# -*- coding: utf-8 -*-
"""Caliopen parameters classes.

All input and ouput parameters of core object methods must
use a class that inherit from of of these.
"""


class BaseReturnObject(object):

    """Base return object."""

    _return_class = None
    _aliases = {}


class ReturnCoreObject(BaseReturnObject):

    """Return object for core instance.

    to define a return object for a core suitable for protocol
    output, inherit from this class defining _core_class,
    _return_class attribute.

    parameter = ReturnObject.build(core)
    parameter.serialize()
    """

    _core_class = None

    @classmethod
    def build(cls, core):
        """Main method to build a return object from a core."""
        kls = cls._return_class
        obj = kls()
        for k, v in obj.serialize().iteritems():
            if cls._aliases.get(k):
                core_key = cls._aliases[k]
            else:
                core_key = k
            attr = getattr(core, core_key)
            if hasattr(cls._core_class, '_relations') \
               and k in cls._core_class._relations:
                attr = [x.to_dict() for x in attr]
            setattr(obj, k, attr)
        obj.validate()
        return obj


class ReturnIndexObject(BaseReturnObject):

    """Return object from index entry.

    Inherit from this class for an index class
    and define which parameter return class to use for build

    parameter = ReturnIndexObject(index_entry)
    parameter.serialize()
    """

    _index_class = None
    _default = {}

    @classmethod
    def build(cls, entry):
        """Main method to build a return object from an index entry."""
        kls = cls._return_class
        obj = kls()
        for k, v in obj.serialize().iteritems():
            if cls._aliases.get(k):
                idx_key = cls._aliases[k]
            else:
                idx_key = k
            attr = entry.get(idx_key, cls._default.get(idx_key))
            setattr(obj, k, attr)
        obj.validate()
        return obj
