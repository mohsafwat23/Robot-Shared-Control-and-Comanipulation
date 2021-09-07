# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from SLERP/Num.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class Num(genpy.Message):
  _md5sum = "17a538d213721bf39aee66a387b311dd"
  _type = "SLERP/Num"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Quaternion q1
geometry_msgs/Quaternion q2
float32 t




================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['q1','q2','t']
  _slot_types = ['geometry_msgs/Quaternion','geometry_msgs/Quaternion','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       q1,q2,t

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Num, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.q1 is None:
        self.q1 = geometry_msgs.msg.Quaternion()
      if self.q2 is None:
        self.q2 = geometry_msgs.msg.Quaternion()
      if self.t is None:
        self.t = 0.
    else:
      self.q1 = geometry_msgs.msg.Quaternion()
      self.q2 = geometry_msgs.msg.Quaternion()
      self.t = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_8df().pack(_x.q1.x, _x.q1.y, _x.q1.z, _x.q1.w, _x.q2.x, _x.q2.y, _x.q2.z, _x.q2.w, _x.t))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.q1 is None:
        self.q1 = geometry_msgs.msg.Quaternion()
      if self.q2 is None:
        self.q2 = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 68
      (_x.q1.x, _x.q1.y, _x.q1.z, _x.q1.w, _x.q2.x, _x.q2.y, _x.q2.z, _x.q2.w, _x.t,) = _get_struct_8df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_8df().pack(_x.q1.x, _x.q1.y, _x.q1.z, _x.q1.w, _x.q2.x, _x.q2.y, _x.q2.z, _x.q2.w, _x.t))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.q1 is None:
        self.q1 = geometry_msgs.msg.Quaternion()
      if self.q2 is None:
        self.q2 = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 68
      (_x.q1.x, _x.q1.y, _x.q1.z, _x.q1.w, _x.q2.x, _x.q2.y, _x.q2.z, _x.q2.w, _x.t,) = _get_struct_8df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8df = None
def _get_struct_8df():
    global _struct_8df
    if _struct_8df is None:
        _struct_8df = struct.Struct("<8df")
    return _struct_8df
