class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    
    def mark_done(self):
        self.done = True
    
    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"])
        if data.get("done", False):
            task.mark_done()
        return task

t1 = Task("Buy milk")
t2 = Task("Mow lawn")
t1.mark_done()
print(t1)
print(t2)