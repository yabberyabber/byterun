STRICT = 1
WARN = 2

class Issue(BaseException):
    def __repr__(self):
        return ('%s: "%s"' % (type(self), str(self)))

class TypeChange(Issue):
    def __init__(self, oldType, newType, identifier, context=None):
        self.oldType = oldType
        self.newType = newType
        self.identifier = identifier

    def __str__(self):
        return (
            ("Type change:  variable %s was type %s, " +
             "now is type %s") %
            (str(self.oldType), str(self.newType),
             self.identifier))

    def __eq__(self, that):
        return (self.oldType == that.oldType and
                self.newType == that.newType and
                self.identifier == that.identifier)

    def __hash__(self):
        return hash(str(self))

class DictionaryIter(Issue):
    def __init__(self):
        pass

    def __str__(self):
        return ("Tried to iterate over a dictionary without " +
                "explicitly calling")

    def __eq__(self, that):
        return type(self) == type(that)

    def __hash__(self):
        return hash(str(self))

class ModConst(Issue):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return ("Modified a variable whos name is in all caps: %s" %
                (self.identifier, ))

    def __eq__(self, that):
        return type(self) == type(that) and self.identifier == that.identifier

    def __hash__(self):
        return hash(str(self))

class BannedFunction(Issue):
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return "Called a banned function: %s" % (self.func, )

    def __eq__(self, that):
        return type(self) == type(that) and self.func == that.func

    def __hash__(self):
        return hash(str(self))
