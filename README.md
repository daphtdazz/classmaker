# classmaker

Make complex classes avoiding metaclass conflicts.

## Rationale

Python sometimes cops out of building a class when you were intuitively expecting there to be no problems. The classic situation is as follows:

    >>> from six import add_metaclass
    >>> class MetaClassA(type):
    ...     pass

    >>> class MetaClassB(type):
    ...     pass

    >>> class BaseClassA(metaclass=MetaClassA):
    ...     pass

    >>> class BaseClassB(metaclass=MetaClassB):
    ...     pass

    >>> class MyClass(BaseClassA, BaseClassB):
    ...     pass
    Traceback (most recent call last):
    TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

Creating the last class raises `TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases` (on python2 and python3), because python refuses to guess exactly what you wanted the metaclass of `MyClass` to be (should it be `class MetaClass(MetaClassA, MetaClassB)`, or `class MetaClass(MetaClassA, MetaClassB)`, for example).

However, 99% of the time, you don't really care, you just want it to work, generally because the metaclasses are unrelated. `classmaker` will make the decision for you! This is what it looks like (using the class hierarchy above):

    >>> from classmaker import classbuilder

    >>> @classbuilder(bases=(BaseClassA, BaseClassB))
    ... class MyClass:
    ...    pass

    >>> assert isinstance(MyClass, MetaClassA)
    >>> assert isinstance(MyClass, MetaClassB)

    >>> mc = MyClass()
    >>> assert isinstance(mc, BaseClassA)
    >>> assert isinstance(mc, BaseClassB)

## Credits

The smart bit of this was written by Michele Simionato in his recipe [solving the metaclass conflict](http://code.activestate.com/recipes/204197-solving-the-metaclass-conflict/). David Park packaged this up and add the somewhat more convenient `@classbuilder` decorator.
