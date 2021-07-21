from .models import Group, Student, Panelist, Defense, Rubric
from datetime import datetime, timedelta, date, time
import random
from . import db


def populate_group():
    new_group = Group(name='TECH-9', 
                      project_title='LAKBAY: A 3D Philippine Mythological Beat ‘em Up Mobile Game', 
                      program='BSIT-AGD')
    db.session.add(new_group)
    new_group = Group(name='Technopunk', 
                      project_title='Sanity: A 3D Psychological Horror Mystery Adventure PC Game', 
                      program='BSIT-AGD')
    db.session.add(new_group)
    new_group = Group(name='SADISTICS', 
                      project_title='Tales of Ibong Adarna: A Philippine Literature RPG Hack n Slash PC Game', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='FBF Technologies', 
                      project_title='E.S.C. Key: A Detective Escape Room 3D Video Game for PC', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='ILM', 
                      project_title='Adventures of Tammy: Play your stories, An Interactive Storytelling Mobile Game with Augmented Reality Story Playback', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='BRY', 
                      project_title='Tela Nobela: A 2D Filipiniana Dress Up Game and Interactive Storybook of Filipino Fairy Tales', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='B Lancer', 
                      project_title='iBuild: A Game Development using 3D Menu Base Game Simulator', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Archi-Tech', 
                      project_title='Odditiseum: A Virtual Reality Point-and-Click Exploration PC Game', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='SADdle', 
                      project_title='Pipeline A Web-based PC Hardware and Peripheral Data-driven price Comparison', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Sleep Deprived', 
                      project_title='Stratics: A Web-Based Churn Analytics Platform for Strategic Decision Making of Telecommunications Companies', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='LinkodPinas', 
                      project_title='StarTouch: The Transition to an Inventory System with Digitized Ordering for Starlite Ferries.', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='BLACK-CHEVY', 
                      project_title='MedList: Development of Sales and Inventory Management System for Drug Store using Descriptive Analytics', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='The Backyardigans', 
                      project_title='Enhancing Customer Experience through E-Commerce Sentiment Analysis', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='HouseMates', 
                      project_title='Profit Optimization using a web-based sales and Inventory Dashboard for Small Enterprises', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='UPTECH', 
                      project_title='CryptSim: A Mobile Application with Advanced Cryptocurrency Trading Simulaton', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='SAD Devs', 
                      project_title='Game Credits PH: An E-loading Website for Mobile and Computer Games', 
                      program='BSCS')
    db.session.add(new_group)
    new_group = Group(name='Business Bros', 
                      project_title='BeFit: A Web and Mobile-Based Marketplace for Integrated Fitness & Wellness.', 
                      program='BSCS')
    db.session.add(new_group)
    db.session.commit()

def populate_students():
    x = 1
    student1 = Student(last_name='Lora', 
                       first_name='Cedric James',
                       middle_in='S',
                       group_id=x)
    student2 = Student(last_name='Balisalisa', 
                       first_name='Joseph Charles',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Fabian', 
                       first_name='Julian Erick Pixel',
                       middle_in='S',
                       group_id=x)
    student4 = Student(last_name='Gonzales', 
                       first_name='Patrick',
                       middle_in='G',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Carmona', 
                       first_name='Josh',
                       middle_in='B',
                       group_id=x)
    student2 = Student(last_name='Aguilar', 
                       first_name='Jaro Alexander',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Dapitan', 
                       first_name='Dominic',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Quesada', 
                       first_name='Maynard',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Avila', 
                       first_name='Josiah Ariel',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Yun', 
                       first_name='Jae Young',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Bustamante', 
                       first_name='Christian Paul',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Matushita', 
                       first_name='Kenichi',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Quijano', 
                       first_name='Jonas Matthew',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Osugui', 
                       first_name='Vianni Tetsuya',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Garcia', 
                       first_name='Trisha Ghael',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Masaya', 
                       first_name='Jhan Jethrix',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Nuñez', 
                       first_name='LA',
                       middle_in='D',
                       group_id=x)
    student2 = Student(last_name='Camaña', 
                       first_name='Gia Fiel',
                       middle_in='O',
                       group_id=x)
    student3 = Student(last_name='Libunao', 
                       first_name='Christian Arvee',
                       middle_in='R',
                       group_id=x)
    student3 = Student(last_name='Vasquez', 
                       first_name='Jash Mhaynard',
                       middle_in='M',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Espela', 
                       first_name='Ysabelle Beatrice',
                       middle_in='L',
                       group_id=x)
    student2 = Student(last_name='Castro', 
                       first_name='Ryan James',
                       middle_in='D',
                       group_id=x)
    student3 = Student(last_name='Mijares', 
                       first_name='Jasmine Fay',
                       middle_in='O',
                       group_id=x)
    student4 = Student(last_name='Salas', 
                       first_name='Arianne',
                       middle_in='J',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Garcia', 
                       first_name='Kyle Joseph Edward',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Arquelita', 
                       first_name='Francis Charles',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Rueda', 
                       first_name='Lance Gabriel',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Biteng', 
                       first_name='Judi Lionie',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1
    
    student1 = Student(last_name='Galos', 
                       first_name='Aaron David',
                       middle_in='D',
                       group_id=x)
    student2 = Student(last_name='Sevilla', 
                       first_name='Mario Gabriel',
                       middle_in='Q',
                       group_id=x)
    student3 = Student(last_name='Pilapit,', 
                       first_name='Keene Lester',
                       middle_in='A',
                       group_id=x)
    student4 = Student(last_name='Poon', 
                       first_name='Ron Edward',
                       middle_in='C',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Cacanindin', 
                       first_name='Marbien',
                       middle_in='C',
                       group_id=x)
    student2 = Student(last_name='Bueneventura', 
                       first_name='Juwon Zeht',
                       middle_in='B',
                       group_id=x)
    student3 = Student(last_name='Amor', 
                       first_name='Nicholas James',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Torres', 
                       first_name='Eugene',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Sancon', 
                       first_name='Deinielle',
                       middle_in='M',
                       group_id=x)
    student2 = Student(last_name='Delos Santos', 
                       first_name='Alyssa Kirsten',
                       middle_in='S',
                       group_id=x)
    student3 = Student(last_name='Malapit', 
                       first_name='Shandon France',
                       middle_in='R',
                       group_id=x)
    student4 = Student(last_name='Solis', 
                       first_name='Amirah Faye',
                       middle_in='B',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Sabbun', 
                       first_name='Stephen John',
                       middle_in='C',
                       group_id=x)
    student2 = Student(last_name='Germina', 
                       first_name='Chester Lord',
                       middle_in='S',
                       group_id=x)
    student3 = Student(last_name='Mercado', 
                       first_name='Ewen Kyle',
                       middle_in='C',
                       group_id=x)
    student4 = Student(last_name='Alcantara', 
                       first_name='Joshua',
                       middle_in='H',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1
    
    student1 = Student(last_name='Argana IV', 
                       first_name='Edgardo Rommel',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Mariquit', 
                       first_name='Lorenz',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Custodio', 
                       first_name='Emil',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Lantacon', 
                       first_name='John Lemuel',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Yason', 
                       first_name='Maria Darlene',
                       middle_in='C',
                       group_id=x)
    student2 = Student(last_name='Consulta', 
                       first_name='Carle Anette',
                       middle_in='C',
                       group_id=x)
    student3 = Student(last_name='Manansala', 
                       first_name='Joseph Enrico Paolo',
                       middle_in='E',
                       group_id=x)
    student4 = Student(last_name='Ponsones', 
                       first_name='Jose Miguel',
                       middle_in='R',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Jarme', 
                       first_name='Anne Raphaelle',
                       middle_in='O',
                       group_id=x)
    student2 = Student(last_name='Hernandez', 
                       first_name='Ezra',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Labandera', 
                       first_name='Ivan',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Sarte', 
                       first_name='Clarence Grendel',
                       middle_in='M',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Monis', 
                       first_name='Camille',
                       middle_in='L',
                       group_id=x)
    student2 = Student(last_name='Galay', 
                       first_name='Isaiah Thomas',
                       middle_in='A',
                       group_id=x)
    student3 = Student(last_name='Narag', 
                       first_name='Charles Dominic',
                       middle_in='R',
                       group_id=x)
    student4 = Student(last_name='Paje', 
                       first_name='Micahel John',
                       middle_in='D.V.',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Yu', 
                       first_name='Daniel Edison',
                       middle_in='',
                       group_id=x)
    student2 = Student(last_name='Carubio', 
                       first_name='Kenneth Christian',
                       middle_in='',
                       group_id=x)
    student3 = Student(last_name='Fenol', 
                       first_name='Lance Mark',
                       middle_in='',
                       group_id=x)
    student4 = Student(last_name='Lugay', 
                       first_name='Miguel',
                       middle_in='',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Ferreria', 
                       first_name='Elijah Rei',
                       middle_in='A',
                       group_id=x)
    student2 = Student(last_name='Goyon', 
                       first_name='Michael Joseph',
                       middle_in='F',
                       group_id=x)
    student3 = Student(last_name='Lustre', 
                       first_name='Nikko Andre',
                       middle_in='C',
                       group_id=x)
    student4 = Student(last_name='Uy', 
                       first_name='Patrick Jerome',
                       middle_in='A',
                       group_id=x)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

def populate_panelist():
    new_panel = Panelist(last_name='Bombasi',
                         username='bombasi_a',
                         password='bombasijoferson',
                         first_name='Joferson',
                         middle_in='L',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Moso',
                         username='moso_a',
                         password='mosomelvin',
                         first_name='Melvin',
                         middle_in='F',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Carpio',
                         username='carpio_a',
                         password='carpioailene',
                         first_name='Ailene',
                         middle_in='B',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Pempina',
                         username='pempina_t',
                         password='pempinaeymard',
                         first_name='Eymard',
                         middle_in='B',
                         school='FEU Tech')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Almeniana',
                         username='almeniana_a',
                         password='almenianafanny',
                         first_name='Fanny',
                         middle_in='C',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Ortega',
                         username='ortega_a',
                         password='ortegomilagros',
                         first_name='Milagros',
                         middle_in='V',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Juanatas',
                         username='juanatas_t',
                         password='juanatasiris',
                         first_name='Iris',
                         middle_in='C',
                         school='FEU Tech')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Abacan',
                         username='abacan_a',
                         password='abacanraycarlo',
                         first_name='Ray Carlo',
                         middle_in='A',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Oderon',
                         username='oderon_a',
                         password='oderonpaula',
                         first_name='Pauline',
                         middle_in='B',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Tiao',
                         username='tiao_a',
                         password='tiaoian',
                         first_name='Ian',
                         middle_in='L',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Lalata',
                         username='lalata_t',
                         password='lalatajay-ar',
                         first_name='Jay-Ar',
                         middle_in='',
                         school='FEU Tech')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Lagman',
                         username='lagman_t',
                         password='lagmanace',
                         first_name='Ace',
                         middle_in='C',
                         school='FEU Tech')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Grimaldo',
                         username='grimaldo_a',
                         password='grimaldohoneylet',
                         first_name='Honeylet',
                         middle_in='',
                         school='FEU Alabang')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Adao',
                         username='adao_t',
                         password='adaorossana',
                         first_name='Rossana',
                         middle_in='A',
                         school='FEU Tech')
    db.session.add(new_panel)

    new_panel = Panelist(last_name='Ricafrente',
                         username='ricafrente_a',
                         password='ricafrentemichael',
                         first_name='Michael',
                         middle_in='R',
                         school='FEU Alabang')
    db.session.add(new_panel)

    db.session.commit()

def populate_defense():
    arr = []
    panels = Panelist.query.all()
    x = 1
    for panel in panels:
        arr.append(panel)
    
    start_date = datetime(2021, 7, 6, 13, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[1])
    new_defense.panels.append(arr[2])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 6, 14, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=4
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[3])
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[2])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 6, 15, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[1])
    new_defense.panels.append(arr[4])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 6, 16, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=7
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[6])
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[4])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 9, 13, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[5])
    new_defense.panels.append(arr[8])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 9, 14, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[5])
    new_defense.panels.append(arr[7])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 9, 15, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=4
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[3])
    new_defense.panels.append(arr[8])
    new_defense.panels.append(arr[0])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 9, 16, 00, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=7
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[6])
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[9])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 8, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=11
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[10])
    new_defense.panels.append(arr[2])
    new_defense.panels.append(arr[0])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 9, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=12
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[11])
    new_defense.panels.append(arr[13])
    new_defense.panels.append(arr[5])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 10, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=13
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[12])
    new_defense.panels.append(arr[9])
    new_defense.panels.append(arr[0])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 11, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=11
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[10])
    new_defense.panels.append(arr[4])
    new_defense.panels.append(arr[0])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 13, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=12
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[11])
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[14])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 14, 14, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[4])
    new_defense.panels.append(arr[14])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 16, 15, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=13
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[12])
    new_defense.panels.append(arr[7])
    new_defense.panels.append(arr[0])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 16, 15, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[14])
    new_defense.panels.append(arr[7])
    db.session.commit()
    x += 1

    start_date = datetime(2021, 7, 1, 16, 17, 00)
    end_date = start_date + timedelta(hours=1)
    new_defense = Defense(
        group_id=x, 
        start_date=start_date, 
        end_date=end_date,
        head_panel_id=1
    )
    db.session.add(new_defense)
    new_defense.panels.append(arr[0])
    new_defense.panels.append(arr[4])
    new_defense.panels.append(arr[14])
    db.session.commit()
    x += 1

    # for x in range(1, 11):
    #     if x == 7:
    #         date_temp  = date.fromisoformat('2021-07-14')
    #         time_temp  = time.fromisoformat('15:00:00')
    #     arr = []
    #     while len(arr) != 3:
    #         panel = db.session.query(Panelist).filter_by(id=random.randint(1, 5)).first()
    #         if panel not in arr:
    #             arr.append(panel)
    #     start_date = datetime.combine(date_temp, time_temp)
    #     end_date = start_date + timedelta(hours=1)
    #     time_temp = time.fromisoformat(end_date.strftime('%H:%M:%S'))

    #     new_defense = Defense(
    #         group_id=x, 
    #         start_date=start_date, 
    #         end_date=end_date, 
    #         head_panel_id=random.choice(arr).id
    #     )
    #     db.session.add(new_defense)
    #     new_defense.panels.append(arr[0])
    #     new_defense.panels.append(arr[1])
    #     new_defense.panels.append(arr[2])
    #     db.session.commit()

def populate_rubric():
    temp = Rubric(
        desc='Subject Mastery',
        rate5='Student discusses the subject with enough information, provides supporting details and gives specific examples.',
        rate4='Student discusses the subject with enough information and supporting details.',
        rate3='Student discusses the subject with enough information. ',
        rate2='Student discusses the subject with very minimal details during the discussion.',
        rate1='Student has no subject mastery at all.',
        weight=8,
        rubric_type='Individual',
        category='None',
        pbl_lvl='None'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Ability to Answer Questions',
        rate5='Student can answer all questions about the subject and can explain thoroughly.',
        rate4='Student can answer most questions about the subject.',
        rate3='Student can answer some questions about the subject.',
        rate2='Student can answer few questions about the subject.',
        rate1='Student cannot answer any question about the subject.',
        weight=6,
        rubric_type='Individual',
        category='None',
        pbl_lvl='None'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Delivery',
        rate5='Student shows very excellent gestures and expressions to convey ideas.',
        rate4='Student shows very good gestures and expressions to convey ideas.',
        rate3='Student shows good gestures and expressions to convey ideas.',
        rate2='Student shows gestures and expressions that needs improvement to convey ideas.',
        rate1='Student show poor gestures and expressions to convey ideas.',
        weight=2,
        rubric_type='Individual',
        category='None',
        pbl_lvl='None'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Verbal and Non Verbal Ability',
        rate5='Correct grammar, pronunciation, choice of words and use of the English language in general are exceptional.',
        rate4='Correct grammar, pronunciation, choice of words and use of the English language in general are good.',
        rate3='Correct grammar, pronunciation, choice of words and use of the English language in general are acceptable. ',
        rate2='Correct grammar, pronunciation, choice of words, and use of the English language are acceptable, with some flaws.',
        rate1='Correct grammar, pronunciation, choice of words and use of the English language in general are rarely observed.',
        weight=2,
        rubric_type='Individual',
        category='None',
        pbl_lvl='None'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Grooming',
        rate5='Student wears formal attire and appears professional, well groomed, and decent.',
        rate4='Student appears professional and decent.',
        rate3='Student is well-groomed and in corporate attire.',
        rate2='Appearance is unprofessional but attempts have been made to look decent.',
        rate1='Appearance is unprofessional.',
        weight=2,
        rubric_type='Individual',
        category='None',
        pbl_lvl='None'
    )
    db.session.add(temp)

    db.session.commit()

