# encoding: utf-8

"""
设计模式：行为型
14.观察者模式

定义类一种一对多的依赖，让多个观察者对象同时监听某一个主题对象
这个主题对象在发生变化时，会通知所有观察者对象，使得它们能够自动更新自己

- 适用：当一个对象的改变需要同时进行改变其他对象时
- 解耦合：让耦合的双方依赖于抽象，而不是依赖具体
"""

from abc import ABCMeta, abstractmethod



class Subject(object):
    """
    把所有对观察者对象的引用保存到一个聚集里
    每个主题都可以有任意数量的观察者

    抽象主题体提供了接口增加/删除观察者对象
    """
    def __init__(self):
        self.__observer = []

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for o in self.__observer:
            o.update()

class ConcreteSubject(Subject):
    """
    具体主题，将有关状态存入具体的观察者对象
    在具体注意的内部状态进行改变时，给所有登记过的观察者发出通知
    """
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

class Observer(metaclass = ABCMeta):
    """
    抽象观察者，为所有具体观察者定义接口，在得到主题的统治时，更新自己
    """
    @abstractmethod
    def update(self):
        pass

class ConcreteObserver(Observer):
    """
    具体观察者，实现抽象观察者锁要求的更新接口
    以使本身的状态于主题的状态协调
    """
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.objserver_status = None

    def update(self):
        self.objserver_status = self.subject.status
        print("the observer: %s status change to %s" % (self.name, self.objserver_status))

if __name__ == '__main__':
    s = ConcreteSubject()

    s.attach(ConcreteObserver(s, "X"))
    s.attach(ConcreteObserver(s, "Y"))
    s.attach(ConcreteObserver(s, "Z"))

    s.status = "A"
    s.notify()

    s.status = "B"
    s.notify()
