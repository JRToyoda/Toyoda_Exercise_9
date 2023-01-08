class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.body = []

    def addLine(self, line):
        self.body.append(line)

    def getText(self):
        text = "Dear " + self.letterTo + ":\n"
        text += "\n"

        for line in self.body:
            text = text + line + "\n"
            text += "\n"

        text += "Sincerely,\n\n"
        text += self.letterFrom

        return text
