import random


class Entity:
    cnt = 1

    def __init__(self, title='Simple title', author='No author'):
        self.id = self.cnt
        self.title = title
        self.author = author
        self.__class__.cnt += 1

    def __del__(self):
        self.__class__.cnt -= 1

class Document(Entity):
    pass

class Section(Entity):
    pass

class DocumentInSection:
    cnt = 1

    def __init__(self, section_id=None, document_id=None):
        self.id = self.cnt
        self.section_id = section_id
        self.document_id = document_id
        self.__class__.cnt += 1

    def __del__(self):
        self.__class__.cnt -= 1


sections = [
    Section('Desktop', 'Egor'),
    Section('Trash', 'Egor'),
    Section('Downloads', 'Egor'),
]

documents = [
    Document('РК-1', 'Egor'),
    Document('PK-2', 'Egor'),
    Document('Steam', 'Egor'),
]

# Да может появиться два одинаковых документа, но будем считать что это копии
documents_in_sections = [
    DocumentInSection(random.choice(sections).id, random.choice(documents).id),
    DocumentInSection(random.choice(sections).id, random.choice(documents).id),
    DocumentInSection(random.choice(sections).id, random.choice(documents).id),
]

key_word = 'D'
sec_dict = {
     sec.title: [d_in_s.document_id for d_in_s in documents_in_sections if d_in_s.section_id == sec.id] for sec in sections if key_word in sec.title
}
result = {
    title: [doc.title for doc in documents if doc.id in data] for title, data in sec_dict.items()
}

print('Задание №3')
for section_title, docs in result.items():
    print(f"Раздел: {section_title}")
    for doc_title in docs:
        print(f"  Документ: {doc_title}")