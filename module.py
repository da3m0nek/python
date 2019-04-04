import datetime

class Note:
  IDn=0

  def __init__(self, text, tag):
    self.text=text
    self.tag=tag
    self.id=Note.IDn
    Note.IDn+=1
    self.date=datetime.datetime.now()
  
  def match(self, str):
    if str in self.text or str in self.tag:
      return True
    else:
      return False

  def __str__(self):
    return f"Id: {self.id} text: {self.text} tag: {self.tag}, date: {self.date}"


class Notebook:


  def __init__(self):
    self.notes = []

  def new_note(self, txt, tag):
      note= Note(txt,tag)
      self.notes.append(note)

  def modify_text(self,id):
      text=input("new text: ")
      self.notes[id].text= text

  def modify_tag(self,id):
      tag=input("new tag: ")
      self.notes[id].tag=tag

  def search(self,str):
      search_notes= []
      for x in range(self.notes):
        if str in x.text or str in x.tag:
          search_notes.append(x)
      return search_notes

  def getNotes(self):
    print(*self.notes, sep='\n')
    






