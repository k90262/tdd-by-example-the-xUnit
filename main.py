class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()

    def setUp(self):
        pass

    def tearDown(self):
        pass

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

    def testFailed(self):
        self.errorCount += 1


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception

class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResultFormatting(self):
        test = TestResult()
        test.testStarted()
        test.testFailed()
        assert ("1 run, 1 failed" == test.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert ("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert ("2 run, 1 failed" == result.summary())

if __name__ == '__main__':
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
