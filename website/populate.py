from .models import Group, Student, Panelist, Defense
from datetime import datetime, timedelta, date, time
import random
from . import db

def populate_group():
    new_group = Group(name='OHRCa', 
                      project_title='Maria', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Sagip', 
                      project_title='Sagip', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Game Balancing', 
                      project_title='Game Balancing', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Sign Language', 
                      project_title='Sign Language', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Pose Estimation', 
                      project_title='Post Estimation', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='KYON', 
                      project_title='KYON', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='BISKWIT', 
                      project_title='BISKWIT', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='CryptoBank', 
                      project_title='CryptoBank', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Data Analysis', 
                      project_title='Data Analysis', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='TV Commercials', 
                      project_title='TV Commercials', 
                      program='BSCS')
    db.session.add(new_group)
    db.session.commit()

def populate_students():
    x = 1
    student1 = Student(last_name='Reyes', 
                       first_name='Charles Kyle',
                       middle_in='A',
                       group_id=x)
    student2 = Student(last_name='Cal', 
                       first_name='Andre Daniel',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Hadjimanan', 
                       first_name='Al-Noor',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Ontuca', 
                       first_name='Angelica',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Ermino', 
                       first_name='Ronnel',
                       middle_in='P',
                       group_id=x)
    student2 = Student(last_name='Diamante', 
                       first_name='Nadine Gweneth',
                       middle_in='C',
                       group_id=x)
    student3 = Student(last_name='Faca', 
                       first_name='Kristine Marie',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Juntereal', 
                       first_name='Thatiana Erica',
                       middle_in='D',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Sambat', 
                       first_name='Immanuel',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Asi', 
                       first_name='Joshua',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Lapuz', 
                       first_name='CJ',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Galicha', 
                       first_name='Romar',
                       middle_in='R',
                       group_id=x)
    student2 = Student(last_name='Quijano', 
                       first_name='John Neiro',
                       middle_in='P',
                       group_id=x)
    student3 = Student(last_name='Barreto', 
                       first_name='Tyrone Maximus',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Liao', 
                       first_name='Paulo Miguel',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Basibas', 
                       first_name='Kenneth Ryan',
                       middle_in='B',
                       group_id=x)
    student2 = Student(last_name='Alejandro', 
                       first_name='Carl Justine',
                       middle_in='T',
                       group_id=x)
    student3 = Student(last_name='Ramos', 
                       first_name='King Edrianne Miles',
                       middle_in='A',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Gonda', 
                       first_name='Shane Angelo',
                       middle_in='J',
                       group_id=x)
    student2 = Student(last_name='Magno', 
                       first_name='David',
                       middle_in='G',
                       group_id=x)
    student3 = Student(last_name='Palao', 
                       first_name='Celynne Anne',
                       middle_in='V',
                       group_id=x)
    student4 = Student(last_name='Salandanan', 
                       first_name='Keith Lundberg',
                       middle_in='A',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Barcelon', 
                       first_name='Matthew',
                       middle_in='N',
                       group_id=x)
    student2 = Student(last_name='Alde', 
                       first_name='Adrian Juls',
                       middle_in='M',
                       group_id=x)
    student3 = Student(last_name='Baldueza', 
                       first_name='Liam',
                       middle_in='D',
                       group_id=x)
    student4 = Student(last_name='Elizarde', 
                       first_name='Chasey Larisse',
                       middle_in='V',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1
    
    student1 = Student(last_name='Taningco', 
                       first_name='Martin Carlo',
                       middle_in='B',
                       group_id=x)
    student2 = Student(last_name='Alarcon', 
                       first_name='Marian Anika',
                       middle_in='T',
                       group_id=x)
    student3 = Student(last_name='Arcon,', 
                       first_name='Einar Gabriel',
                       middle_in='H',
                       group_id=x)
    student4 = Student(last_name='Astrero', 
                       first_name='John Michael',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Jovellano', 
                       first_name='Jens Gabriel',
                       middle_in='T',
                       group_id=x)
    student2 = Student(last_name='Lara', 
                       first_name='Ron',
                       middle_in='T',
                       group_id=x)
    student3 = Student(last_name='Lantano,', 
                       first_name='Kelsey',
                       middle_in='R',
                       group_id=x)
    student4 = Student(last_name='Erepol', 
                       first_name='Jovey Ann',
                       middle_in='T',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Guingona', 
                       first_name='Timothy Isaiah',
                       middle_in='B',
                       group_id=x)
    student2 = Student(last_name='Pinera', 
                       first_name='Beatrice',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Nerpio,', 
                       first_name='Lulwah',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Whitegfoot', 
                       first_name='Ryan James',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

def populate_panelist():
    new_panel = Panelist(last_name='Abacan',
                         username='abacan_a',
                         password='alabang1',
                         first_name='Ray Carlo',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Aldana',
                         username='aldana_a',
                         password='alabang2',
                         first_name='Resty',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Ortega',
                         username='ortega_a',
                         password='alabang3',
                         first_name='Miles',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Almeniana',
                         username='almeniana_a',
                         password='alabang4',
                         first_name='Fanny',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Carpio',
                         username='carpio_a',
                         password='alabang5',
                         first_name='Ailene',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    db.session.commit()

def populate_defense():
    date_temp  = date.fromisoformat('2021-07-07')
    time_temp  = time.fromisoformat('13:00:00')
    for x in range(1, 11):
        if x == 7:
            date_temp  = date.fromisoformat('2021-07-14')
            time_temp  = time.fromisoformat('15:00:00')
        arr = []
        while len(arr) != 3:
            panel = db.session.query(Panelist).filter_by(id=random.randint(1, 5)).first()
            if panel not in arr:
                arr.append(panel)
        start_date = datetime.combine(date_temp, time_temp)
        end_date = start_date + timedelta(hours=1)
        time_temp = time.fromisoformat(end_date.strftime('%H:%M:%S'))

        new_defense = Defense(
            group_id=x, 
            start_date=start_date, 
            end_date=end_date, 
            head_panel_id=random.choice(arr).id
        )
        db.session.add(new_defense)
        new_defense.panels.append(arr[0])
        new_defense.panels.append(arr[1])
        new_defense.panels.append(arr[2])
        db.session.commit()