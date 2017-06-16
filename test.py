from classmaker import classbuilder
from pytest import raises
from six import add_metaclass


def build_class_using_classbuilder(bases, metaclasses):

    @classbuilder(bases=bases, mc=metaclasses)
    class MyClass:
        pass

    return MyClass


def test_one_base_one_metaclass():

    class MetaClassA(type):
        pass

    class BaseClassA:
        pass

    MyClass = build_class_using_classbuilder((BaseClassA,), (MetaClassA,))

    assert isinstance(MyClass, MetaClassA)
    mc = MyClass()
    assert isinstance(mc, BaseClassA)


def test_one_base_with_metaclass_and_one_metaclass():

    class MetaClassA(type):
        pass

    @add_metaclass(MetaClassA)
    class BaseClassA:
        pass

    class MetaClassB(type):
        pass

    MyClass = build_class_using_classbuilder((BaseClassA,), (MetaClassB,))

    assert isinstance(MyClass, MetaClassA)
    assert isinstance(MyClass, MetaClassB)
    mc = MyClass()
    assert isinstance(mc, BaseClassA)


def test_two_bases_each_with_metaclasses():

    class MetaClassA(type):
        def do_something(self):
            pass

    @add_metaclass(MetaClassA)
    class BaseClassA:
        pass

    class MetaClassB(type):
        def do_something_else(self):
            pass

    @add_metaclass(MetaClassB)
    class BaseClassB:
        pass

    # demonstrate that we are actually doing something useful...
    with raises(TypeError, match='metaclass conflict'):
        def attempt_standard_class_build():
            class MyClass(BaseClassA, BaseClassB):
                pass

        attempt_standard_class_build()

    MyClass = build_class_using_classbuilder((BaseClassA, BaseClassB), ())
    assert isinstance(MyClass, MetaClassB)
    assert isinstance(MyClass, MetaClassA)

    MyClass = build_class_using_classbuilder((BaseClassB, BaseClassA), ())
    assert isinstance(MyClass, MetaClassB)
    assert isinstance(MyClass, MetaClassA)
