"""
A Cooler is a P controller 
Author: Elias Bakken
email: elias(dot)bakken(at)gmail(dot)com
Website: http://www.thing-printer.com
License: GNU GPL v3: http://www.gnu.org/copyleft/gpl.html

 Redeem is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Redeem is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Redeem.  If not, see <http://www.gnu.org/licenses/>.
"""

from threading import Thread, Event
import logging


class Cooler:
  def __init__(self, cold_end, fan, name, onoff_control):
    """ Init """
    self.cold_end = cold_end
    self.fan = fan
    self.name = name    # Name, used for debugging
    self.current_temp = 0.0
    self.target_temp = 0.0    # Target temperature (Ts). Start off.
    self.P = 1.0    # Proportional
    self.onoff_control = onoff_control    # If we use PID or ON/OFF control
    self.max_speed = 1.0
    self.ok_range = 4.0
    self.sleep = 1.0

  def set_max_speed(self, speed):
    """ Set the desired max speed of the fan """
    self.max_speed = speed

  def set_target_temperature(self, temp):
    """ Set the desired temperature of the extruder """
    self.target_temp = float(temp)

  def get_temperature(self):
    """ get the temperature of the thermistor"""
    return self.current_temp

  def is_target_temperature_reached(self):
    """ Returns true if the target temperature is reached """
    if self.target_temp == 0:
      return True
    err = abs(self.current_temp - self.target_temp)
    return err < self.ok_range

  def disable(self):
    """ Stops the fan and the PID controller """
    self.stop_thread.set()
    self.t.join()
    logging.debug("Cooler {} disabled".format(self.name))
    self.fan.set_power(0.0)

  def enable(self):
    """ Start the controller """
    self.stop_thread = Event()
    self.t = Thread(target=self.keep_temperature, name=self.name)
    self.t.daemon = True
    self.t.start()

  def set_p_value(self, P):
    """ Set values for Proportional"""
    self.P = P    # Proportional

  def keep_temperature(self):
    """ Thread that keeps the temperature stable """
    while not self.stop_thread.is_set():
      self.current_temp = self.cold_end.get_temperature()
      error = self.target_temp - self.current_temp

      if self.onoff_control:
        power = 1.0 if (self.P * error > 1.0) else 0.0
      else:
        power = self.P * error    # The formula for the PID (only P)
        power = max(min(power, 1.0), 0.0)    # Normalize to 0,1

      # Invert the control since it'a a cooler
      power = 1.0 - power
      # Clamp the max speed
      power = min(power, self.max_speed)
      #logging.debug("Err: {}, Pwr: {}".format(error, power))
      self.fan.set_value(power)
      self.stop_thread.wait(self.sleep)
