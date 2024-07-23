class TestClass:
    def __init__(self, name):
        self.name = name
    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestClass):
    def __init__(self, name):
        self.wasRun = None
        TestClass.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1


if __name__ == '__main__':
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)
