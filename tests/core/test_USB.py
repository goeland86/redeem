# Work in progress - ARC
import unittest
import mock    # use mock.Mock etc
from USB import USB


class TestUSB(unittest.TestCase):
  def setUp(self):
    testUSB = USB()


#
#
#     def test_get_message(self):
#         """ Loop that gets messages and pushes them on the queue """
#         while self.running:
#             ret = select.select([self.tty], [], [], 1.0)
#             if ret[0] == [self.tty]:
#                 message = self.tty.readline().strip("\n")
#                 if len(message) > 0:
#                     g = Gcode({"message": message, "prot": "USB"})
#                     self.printer.processor.enqueue(g)
#                     # Do not enable sending messages until a
#                     # message has been received
#                     self.send_response = True
#
#     def test_send_message(self, message):
#         """ Send a message """
#         if self.send_response:
#             if message[-1] != "\n":
#                 message += "\n"
#             #logging.debug("USB: "+str(message))
#             self.tty.write(message)
#
#     def test_close(self):
#         """ Stop receiving messages """
#         self.running = False
#         if hasattr(self, 't'):
#             self.t.join()
