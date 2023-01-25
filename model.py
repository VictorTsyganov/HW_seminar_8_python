from dataclasses import dataclass

@dataclass
class Journal:
        path: str
        subject: str
        journal = dict()

        def read_db(self) -> dict:
            with open(self.path + '_class.txt', 'r', encoding='UTF-8') as file:
                lines = file.readlines()
            for line in lines:
                if self.subject.lower() == line.strip().split(';')[0].lower():
                    for student in line.strip().split(';')[1].strip().split(', '):
                        self.journal[student.split(':')[0]] = list(
                            map(int, student.split(':')[1].split()))
                    return self.journal
        
        def save_db(self):
            new_file = []
            with open(self.path + '_class.txt', 'r', encoding='UTF-8') as file:
                lines = file.readlines()
            for line in lines:
                if self.subject.lower() != line.strip().split(';')[0].lower():
                    new_file.append(line.strip())
            item = []
            for student, grades in self.journal.items():
                item.append(student + ':' + ' '.join(list(map(str, grades))))
            item = self.subject + ';' + ', '.join(item)
            new_file.append(item)
            with open(self.path + '_class.txt', 'w', encoding='UTF-8') as file:
                file.write('\n'.join(new_file))
