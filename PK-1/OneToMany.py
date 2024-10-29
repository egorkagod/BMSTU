import random

class Entity:
    cnt = 1

    def __init__(self, title='Simple title', author='No author'):
        self.id = self.__class__.cnt
        self.title = title
        self.author = author
        self.__class__.cnt += 1

    def __del__(self):
        self.__class__.cnt -= 1


class Document(Entity):
    def __init__(self, section_id, title='Simple title', author='No author'):
        super().__init__(title, author)
        self.section_id = section_id


class Section(Entity):
    pass

sections = [
    Section('Desktop', 'Egor'),
    Section('Trash', 'Egor'),
    Section('Downloads', 'Egor'),
]

documents = [
    Document(random.choice(sections).id, 'РК-1', 'Egor'),
    Document(random.choice(sections).id, 'PK-2', 'Egor'),
    Document(random.choice(sections).id, 'Steam', 'Egor'),
]

result = {
    section.title: [doc.title for doc in documents if doc.section_id == section.id]
    for section in sections
}

print('Задание №1')
for section_title, docs in result.items():
    print(f"Раздел: {section_title}")
    for doc_title in docs:
        print(f"  Документ: {doc_title}")

print('\nЗадание №2')
result = [(len(docs), section_title, docs) for section_title, docs in result.items()]
for data in sorted(result):
    count, section_title, docs = data
    print(f"Раздел: {section_title} (Размер раздела: {count})")
    for doc_title in docs:
        print(f"  Документ: {doc_title}")
