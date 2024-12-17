import random
import unittest

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

def create_sections_and_documents():
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
    return sections, documents

def group_documents_by_section(sections, documents):
    return {
        section.title: [doc.title for doc in documents if doc.section_id == section.id]
        for section in sections
    }

def print_sections_and_documents(result):
    print('Задание №1')
    for section_title, docs in result.items():
        print(f"Раздел: {section_title}")
        for doc_title in docs:
            print(f"  Документ: {doc_title}")

def print_sorted_sections(result):
    print('\nЗадание №2')
    result = [(len(docs), section_title, docs) for section_title, docs in result.items()]
    for data in sorted(result):
        count, section_title, docs = data
        print(f"Раздел: {section_title} (Размер раздела: {count})")
        for doc_title in docs:
            print(f"  Документ: {doc_title}")

class TestDocumentGrouping(unittest.TestCase):
    def test_group_documents_by_section(self):
        sections = [Section('Desktop', 'Egor'), Section('Trash', 'Egor')]
        documents = [
            Document(sections[0].id, 'Doc1', 'Egor'),
            Document(sections[0].id, 'Doc2', 'Egor'),
            Document(sections[1].id, 'Doc3', 'Egor')
        ]
        result = group_documents_by_section(sections, documents)
        self.assertEqual(result['Desktop'], ['Doc1', 'Doc2'])
        self.assertEqual(result['Trash'], ['Doc3'])

    def test_empty_documents(self):
        sections = [Section('Desktop', 'Egor')]
        documents = []
        result = group_documents_by_section(sections, documents)
        self.assertEqual(result['Desktop'], [])

    def test_no_matching_sections(self):
        sections = [Section('Desktop', 'Egor')]
        documents = [Document(999, 'Doc1', 'Egor')]
        result = group_documents_by_section(sections, documents)
        self.assertEqual(result['Desktop'], [])

if __name__ == "__main__":
    sections, documents = create_sections_and_documents()
    result = group_documents_by_section(sections, documents)
    print_sections_and_documents(result)
    print_sorted_sections(result)
    unittest.main()
