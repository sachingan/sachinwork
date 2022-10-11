class parent:
    def properties(self):
        self.props={"car":"swift","mobile":"nokia n21"}
        return self.props


class child(parent):
    def properties(self):
        props=super().properties()
        props["bike"]="pulsar 200 ns"
        return self.props

sa=child()
print(sa.properties())


class editor:
    def functions(self):
        self.props=["create new file","execute","save"]
        return self.props

class pycharm(editor):
    def functions(self):            #overriding parent functions
        props=super().functions()
        props.append(["debug","versioncontrolling"])
        return props

class vscode(editor):
    def functions(self):
        props=super().functions()
        props.append("more extension support")
        return props

py=pycharm()
print(py.functions())
vsc=vscode()
print(vsc.functions())