from .models import Group, Student, Panelist, Defense, Rubric, Template
from datetime import datetime, timedelta, date, time
import random
from . import db


def populate_group():
    new_group = Group(name='TECH-9', 
                      project_title='LAKBAY: A 3D Philippine Mythological Beat ‘em Up Mobile Game', 
                      program='BSIT-AGD',
                      mentor_id=15)
    db.session.add(new_group)
    new_group = Group(name='Technopunk', 
                      project_title='Sanity: A 3D Psychological Horror Mystery Adventure PC Game', 
                      program='BSIT-AGD',
                      mentor_id=15)
    db.session.add(new_group)
    new_group = Group(name='SADISTICS', 
                      project_title='Tales of Ibong Adarna: A Philippine Literature RPG Hack n Slash PC Game', 
                      program='BSIT-AGD',
                      mentor_id=15)
    db.session.add(new_group)
    new_group = Group(name='FBF Technologies', 
                      project_title='E.S.C. Key: A Detective Escape Room 3D Video Game for PC', 
                      program='BSIT-AGD',
                      mentor_id=15)
    db.session.add(new_group)
    new_group = Group(name='ILM', 
                      project_title='Adventures of Tammy: Play your stories, An Interactive Storytelling Mobile Game with Augmented Reality Story Playback', 
                      program='BSIT-DA',
                      mentor_id=2)
    db.session.add(new_group)
    new_group = Group(name='BRY', 
                      project_title='Tela Nobela: A 2D Filipiniana Dress Up Game and Interactive Storybook of Filipino Fairy Tales', 
                      program='BSIT-DA',
                      mentor_id=9)
    db.session.add(new_group)
    new_group = Group(name='B Lancer', 
                      project_title='iBuild: A Game Development using 3D Menu Base Game Simulator', 
                      program='BSIT-AGD',
                      mentor_id=3)
    db.session.add(new_group)
    new_group = Group(name='Archi-Tech', 
                      project_title='Odditiseum: A Virtual Reality Point-and-Click Exploration PC Game', 
                      program='BSIT-AGD',
                      mentor_id=15)
    db.session.add(new_group)
    new_group = Group(name='SADdle', 
                      project_title='Pipeline A Web-based PC Hardware and Peripheral Data-driven price Comparison', 
                      program='BSIT-SMBA',
                      mentor_id=5)
    db.session.add(new_group)
    new_group = Group(name='Sleep Deprived', 
                      project_title='Stratics: A Web-Based Churn Analytics Platform for Strategic Decision Making of Telecommunications Companies', 
                      program='BSIT-SMBA',
                      mentor_id=8)
    db.session.add(new_group)
    new_group = Group(name='LingkodPinas', 
                      project_title='StarTouch: The Transition to an Inventory System with Digitized Ordering for Starlite Ferries.', 
                      program='BSIT-MBA',
                      mentor_id=5)
    db.session.add(new_group)
    new_group = Group(name='BLACK-CHEVY', 
                      project_title='MedList: Development of Sales and Inventory Management System for Drug Store using Descriptive Analytics', 
                      program='BSIT-SMBA',
                      mentor_id=3)
    db.session.add(new_group)
    new_group = Group(name='The Backyardigans', 
                      project_title='Enhancing Customer Experience through E-Commerce Sentiment Analysis', 
                      program='BSIT-SMBA',
                      mentor_id=8)
    db.session.add(new_group)
    new_group = Group(name='HouseMates', 
                      project_title='Profit Optimization using a web-based sales and Inventory Dashboard for Small Enterprises', 
                      program='BSIT-SMBA',
                      mentor_id=8)
    db.session.add(new_group)
    new_group = Group(name='UPTECH', 
                      project_title='CryptSim: A Mobile Application with Advanced Cryptocurrency Trading Simulaton', 
                      program='BSIT-WMA',
                      mentor_id=6)
    db.session.add(new_group)
    new_group = Group(name='SAD Devs', 
                      project_title='Game Credits PH: An E-loading Website for Mobile and Computer Games', 
                      program='BSIT-WMA',
                      mentor_id=6)
    db.session.add(new_group)
    new_group = Group(name='Business Bros', 
                      project_title='BeFit: A Web and Mobile-Based Marketplace for Integrated Fitness & Wellness.', 
                      program='BSIT-WMA',
                      mentor_id=3)
    db.session.add(new_group)
    db.session.commit()

def populate_students():
    x = 1
    student1 = Student(last_name='Lora', 
                       first_name='Cedric James',
                       middle_in='S',
                       group_id=x,
                       stud_no=201811305)
    student2 = Student(last_name='Balisalisa', 
                       first_name='Joseph Charles',
                       middle_in='',
                       group_id=x,
                       stud_no=201811950)
    student3 = Student(last_name='Fabian', 
                       first_name='Julian Erick Pixel',
                       middle_in='S',
                       group_id=x,
                       stud_no=201811809)
    student4 = Student(last_name='Gonzales', 
                       first_name='Patrick',
                       middle_in='G',
                       group_id=x,
                       stud_no='201811122')
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Carmona', 
                       first_name='Josh',
                       middle_in='B',
                       group_id=x,
                       stud_no=201811920)
    student2 = Student(last_name='Aguilar', 
                       first_name='Jaro Alexander',
                       middle_in='',
                       group_id=x,
                       stud_no=201810797)
    student3 = Student(last_name='Dapitan', 
                       first_name='Dominic',
                       middle_in='',
                       group_id=x,
                       stud_no=201811943)
    student4 = Student(last_name='Quesada', 
                       first_name='Maynard',
                       middle_in='',
                       group_id=x,
                       stud_no=201811944)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Avila', 
                       first_name='Josiah Ariel',
                       middle_in='',
                       group_id=x,
                       stud_no=201811377)
    student2 = Student(last_name='Yun', 
                       first_name='Jae Young',
                       middle_in='',
                       group_id=x,
                       stud_no=201811766)
    student3 = Student(last_name='Bustamante', 
                       first_name='Christian Paul',
                       middle_in='',
                       group_id=x,
                       stud_no=201810044)
    student3 = Student(last_name='Matshshita', 
                       first_name='Kenichi',
                       middle_in='',
                       group_id=x,
                       stud_no=201812166)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Quijano', 
                       first_name='Jonas Matthew',
                       middle_in='',
                       group_id=x,
                       stud_no=201810046)
    student2 = Student(last_name='Osugui', 
                       first_name='Vianni Tetsuya',
                       middle_in='',
                       group_id=x,
                       stud_no=201810050)
    student3 = Student(last_name='Garcia', 
                       first_name='Trisha Ghael',
                       middle_in='',
                       group_id=x,
                       stud_no=201811915)
    student4 = Student(last_name='Masaya', 
                       first_name='Jhan Jethrix',
                       middle_in='',
                       group_id=x,
                       stud_no=201810092)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Nuñez', 
                       first_name='LA',
                       middle_in='D',
                       group_id=x,
                       stud_no=201811747)
    student2 = Student(last_name='Camaña', 
                       first_name='Gia Fiel',
                       middle_in='O',
                       group_id=x,
                       stud_no=201811183)
    student3 = Student(last_name='Libunao', 
                       first_name='Christian Arvee',
                       middle_in='R',
                       group_id=x,
                       stud_no=201811844)
    student3 = Student(last_name='Vasquez', 
                       first_name='Jash Mhaynard',
                       middle_in='M',
                       group_id=x,
                       stud_no=201812122)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Espela', 
                       first_name='Ysabelle Beatrice',
                       middle_in='L',
                       group_id=x,
                       stud_no=201811065)
    student2 = Student(last_name='Castro', 
                       first_name='Ryan James',
                       middle_in='D',
                       group_id=x,
                       stud_no=201811446)
    student3 = Student(last_name='Mijares', 
                       first_name='Jasmine Fay',
                       middle_in='O',
                       group_id=x,
                       stud_no=201810556)
    student4 = Student(last_name='Salas', 
                       first_name='Arianne',
                       middle_in='J',
                       group_id=x,
                       stud_no=201811118)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Garcia', 
                       first_name='Kyle Joseph Edward',
                       middle_in='',
                       group_id=x,
                       stud_no=201811654)
    student2 = Student(last_name='Arquelita', 
                       first_name='Francis Charles',
                       middle_in='',
                       group_id=x,
                       stud_no=201810064)
    student3 = Student(last_name='Rueda', 
                       first_name='Lance Gabriel',
                       middle_in='',
                       group_id=x,
                       stud_no=201899991)
    student4 = Student(last_name='Biteng', 
                       first_name='Judi Lionie',
                       middle_in='',
                       group_id=x,
                       stud_no=201899992)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1
    
    student1 = Student(last_name='Galos', 
                       first_name='Aaron David',
                       middle_in='D',
                       group_id=x,
                       stud_no=201810998)
    student2 = Student(last_name='Sevilla', 
                       first_name='Mario Gabriel',
                       middle_in='Q',
                       group_id=x,
                       stud_no=201811640)
    student3 = Student(last_name='Pilapil', 
                       first_name='Keene Lester',
                       middle_in='A',
                       group_id=x,
                       stud_no=201810557)
    student4 = Student(last_name='Poon', 
                       first_name='Ron Edward',
                       middle_in='C',
                       group_id=x,
                       stud_no=201899993)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Cacanindin', 
                       first_name='Marbien',
                       middle_in='C',
                       group_id=x,
                       stud_no=201810061)
    student2 = Student(last_name='Bueneventura', 
                       first_name='Juwon Zeht',
                       middle_in='B',
                       group_id=x,
                       stud_no=201811976)
    student3 = Student(last_name='Amor', 
                       first_name='Nicholas James',
                       middle_in='',
                       group_id=x,
                       stud_no=201811485)
    student4 = Student(last_name='Torres', 
                       first_name='Eugene',
                       middle_in='',
                       group_id=x,
                       stud_no=201811450)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Sancon', 
                       first_name='Deinielle',
                       middle_in='M',
                       group_id=x,
                       stud_no=201811815)
    student2 = Student(last_name='Delos Santos', 
                       first_name='Alyssa Kirsten',
                       middle_in='S',
                       group_id=x,
                       stud_no=201812036)
    student3 = Student(last_name='Malapit', 
                       first_name='Shandon France',
                       middle_in='R',
                       group_id=x,
                       stud_no=201899994)
    student4 = Student(last_name='Solis', 
                       first_name='Amirah Faye',
                       middle_in='B',
                       group_id=x,
                       stud_no=201899995)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Sabbun', 
                       first_name='Stephen John',
                       middle_in='C',
                       group_id=x,
                       stud_no=201810728)
    student2 = Student(last_name='Germina', 
                       first_name='Chester Lord',
                       middle_in='S',
                       group_id=x,
                       stud_no=201811080)
    student3 = Student(last_name='Mercado', 
                       first_name='Ewen Kyle',
                       middle_in='C',
                       group_id=x,
                       stud_no=201811868)
    student4 = Student(last_name='Alcantara', 
                       first_name='Joshua',
                       middle_in='H',
                       group_id=x,
                       stud_no=201811608)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1
    
    student1 = Student(last_name='Argana', 
                       first_name='Edgardo Rommel IV',
                       middle_in='',
                       group_id=x,
                       stud_no=201810505)
    student2 = Student(last_name='Mariquit', 
                       first_name='Lorenz',
                       middle_in='',
                       group_id=x,
                       stud_no=201811764)
    student3 = Student(last_name='Custodio', 
                       first_name='Emil',
                       middle_in='',
                       group_id=x,
                       stud_no=201810567)
    student4 = Student(last_name='Lantacon', 
                       first_name='John Lemuel',
                       middle_in='',
                       group_id=x,
                       stud_no=201811558)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Yason', 
                       first_name='Maria Darlene',
                       middle_in='C',
                       group_id=x,
                       stud_no=201812059)
    student2 = Student(last_name='Consulta', 
                       first_name='Carle Anette',
                       middle_in='C',
                       group_id=x,
                       stud_no=201812196)
    student3 = Student(last_name='Manansala', 
                       first_name='Joseph Enrico Paolo',
                       middle_in='E',
                       group_id=x,
                       stud_no=201812164)
    student4 = Student(last_name='Ponsones', 
                       first_name='Jose Miguel',
                       middle_in='R',
                       group_id=x,
                       stud_no=201811401)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Jarme', 
                       first_name='Anne Raphaelle',
                       middle_in='O',
                       group_id=x,
                       stud_no=201811135)
    student2 = Student(last_name='Hernandez', 
                       first_name='Ezra',
                       middle_in='',
                       group_id=x,
                       stud_no=201812033)
    student3 = Student(last_name='Labandera', 
                       first_name='Ivan',
                       middle_in='',
                       group_id=x,
                       stud_no=201812087)
    student4 = Student(last_name='Sarte', 
                       first_name='Clarence Grendel',
                       middle_in='M',
                       group_id=x,
                       stud_no=201899996)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Monis', 
                       first_name='Camille',
                       middle_in='L',
                       group_id=x,
                       stud_no=201810649)
    student2 = Student(last_name='Galay', 
                       first_name='Isaiah Thomas',
                       middle_in='A',
                       group_id=x,
                       stud_no=201811046)
    student3 = Student(last_name='Narag', 
                       first_name='Charles Dominic',
                       middle_in='R',
                       group_id=x,
                       stud_no=201811952)
    student4 = Student(last_name='Paje', 
                       first_name='Micahel John',
                       middle_in='D.V.',
                       group_id=x,
                       stud_no=201810018)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Yu', 
                       first_name='Daniel Edison',
                       middle_in='',
                       group_id=x,
                       stud_no=201810032)
    student2 = Student(last_name='Carubio', 
                       first_name='Kenneth Christian',
                       middle_in='',
                       group_id=x,
                       stud_no=201811497)
    student3 = Student(last_name='Fenol', 
                       first_name='Lance Mark',
                       middle_in='',
                       group_id=x,
                       stud_no=201811273)
    student4 = Student(last_name='Lugay', 
                       first_name='Miguel',
                       middle_in='',
                       group_id=x,
                       stud_no=201811771)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    x += 1

    student1 = Student(last_name='Ferreria', 
                       first_name='Elijah Rei',
                       middle_in='A',
                       group_id=x,
                       stud_no=201811214)
    student2 = Student(last_name='Goyon', 
                       first_name='Michael Joseph',
                       middle_in='F',
                       group_id=x,
                       stud_no=201811420)
    student3 = Student(last_name='Lustre', 
                       first_name='Nikko Andre',
                       middle_in='C',
                       group_id=x,
                       stud_no=201811883)
    student4 = Student(last_name='Uy', 
                       first_name='Patrick Jerome',
                       middle_in='A',
                       group_id=x,
                       stud_no=201811708)
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


    new_panel = Panelist(last_name='Aldana',
                         username='Aldana_a',
                         password='aldanaresty',
                         first_name='Resty',
                         middle_in='F',
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

    temp = Rubric(
        desc='Context Relevance to the Field of Study',
        rate5='Provided a highly critical projects context that provides a potentially relevant investigation',
        rate4='Delivered a good context that provides potentially relevant investigation',
        rate3='Provided an acceptable project context worthy of research',
        rate2='Presented project context somewhat related to the field of study',
        rate1='Project context presented is not relevant to the field of study',
        weight=8,
        rubric_type='Group',
        category='None',
        pbl_lvl='PBL1'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Concept & Ideas',
        rate5='Presented project concepts are excellent',
        rate4='Presented project concepts are good',
        rate3='Projects concepts are acceptable',
        rate2='Project concepts are average with some recommendation',
        rate1='Project concepts lack substantial details.',
        weight=5,
        rubric_type='Group',
        category='None',
        pbl_lvl='PBL1'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Feasibility',
        rate5='Project concepts are attainable, measurable and presented with complete evidences',
        rate4='Presented project concepts are attainable, measurable but presented with almost complete evidences',
        rate3='Presented project concepts are either attainable or measurable with some evidences',
        rate2='Presented project concepts are either attainable or measurable with few evidences',
        rate1='The project concepts presented are not feasible',
        weight=7,
        rubric_type='Group',
        category='None',
        pbl_lvl='PBL1'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Background and Rationale of the Study',
        rate5='All pertinent information on the project was provided and explained well.',
        rate4='All pertinent information on the project was provided',
        rate3='Relevant information on the project was provided',
        rate2='Some information on the project was provided',
        rate1='No related information on the project was given',
        weight=1,
        rubric_type='Group',
        category='Chapter 1',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Project Overview',
        rate5='Project overview is clearly explained',
        rate4='Project overview is adequately explained',
        rate3='Project overview is somehow explained',
        rate2='Project overview is not clearly explained',
        rate1='There is no project overview',
        weight=1,
        rubric_type='Group',
        category='Chapter 1',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Relativeness of the Literature',
        rate5='All literature supports the study',
        rate4='Most literature supports the study',
        rate3='Some literature supports the study',
        rate2='Few literatures support the study',
        rate1='No literature supports the study',
        weight=1,
        rubric_type='Group',
        category='Chapter 2',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Synthesis',
        rate5='The synthesis provides excellent analysis of the literature',
        rate4='The synthesis provides very good analysis of the literature',
        rate3='The synthesis provides good analysis of the literature',
        rate2='The synthesis provides impartial analysis of the literature',
        rate1='The synthesis provides poor analysis of the literature',
        weight=1,
        rubric_type='Group',
        category='Chapter 2',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Feasibility',
        rate5='The requirement analysis strongly supports the feasibility of the study',
        rate4='The requirement analysis suitably supports the feasibility of the study',
        rate3='The requirement analysis justly supports the feasibility of the study',
        rate2='Requirement analysis somehow supports the feasibility of the study',
        rate1='Requirement analysis poorly supports the feasibility of the study',
        weight=2,
        rubric_type='Group',
        category='Chapter 3',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Project Development Model',
        rate5='The project development model perfectly fits to the project design',
        rate4='The project development model acceptably fits to the project design',
        rate3='The project development model fairly fits to the project design',
        rate2='The project development model somewhat fits to the project design',
        rate1='The project development model does not fit to the project design',
        weight=1,
        rubric_type='Group',
        category='Chapter 3',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Technicality',
        rate5='The project design provides highly technical solution to the research problem',
        rate4='The project design provides very technical solution to the research problem',
        rate3='The project design provides technical solution to the research problem',
        rate2='The project design provides minimal technical solution to the research problem',
        rate1='The project design provides poor technical solution to the research problem',
        weight=1,
        rubric_type='Group',
        category='Chapter 3',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Project Design',
        rate5='The solution provided is excellent ',
        rate4='The solution provided is very good',
        rate3='The solution provided is fair',
        rate2='The solution provided is insufficient',
        rate1='The solution provided is poor',
        weight=1,
        rubric_type='Group',
        category='Chapter 3',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Formatting and Supporting Documents',
        rate5='The document is well-formatted and presents complete supporting documents',
        rate4='The document is formatted with few blunders and presents almost complete supporting documents',
        rate3='The document is formatted with some blunders and presents some supporting documents',
        rate2='The document is formatted with many blunders and presents few supporting documents',
        rate1='The document is formatted poorly and presents no supporting documents',
        weight=1,
        rubric_type='Group',
        category='Others',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Presented of Proposal Materials',
        rate5='The materials used in the presentation such as tables, charts, and visualization were explained very well.',
        rate4='The materials used in the presentation such as tables, charts, and visualization were explained well.',
        rate3='The materials used in the presentation such as tables, charts, and visualization were explained fairly.',
        rate2='The materials used in the presentation such as tables, charts, and visualization need more explanation.',
        rate1='The materials used in the presentation such as tables, charts, and visualization were explained poorly.',
        weight=2,
        rubric_type='Group',
        category='Design',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Precision and Accuracy of Design',
        rate5='The tables, charts, and visualization were very accurate and precise.',
        rate4='The tables, charts, and visualization were almost accurate and precise.',
        rate3='The tables, charts, and visualization were fair',
        rate2='The tables, charts, and visualization need improvement',
        rate1='The tables, charts, and visualization need overhaul',
        weight=2,
        rubric_type='Group',
        category='Design',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Consistency with the Documentation',
        rate5='All contents of the presentation clearly match the concise thought of the documentation',
        rate4='Most contents of the presentation clearly match the concise thought of the documentation',
        rate3='Some contents of the presentation clearly match the concise thought of the documentation',
        rate2='Few contents of the presentation clearly match the concise thought of the documentation',
        rate1='No contents of the presentation clearly match the concise thought of the documentation',
        weight=3,
        rubric_type='Group',
        category='Presentation',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    temp = Rubric(
        desc='Flow and Group Dynamics',
        rate5='The presentation is smooth and continuous',
        rate4='The presentation is smooth and continuous minimal interruptions',
        rate3='The group presentation is average',
        rate2='The group presentation needs improvement',
        rate1='The group presentation is unacceptable',
        weight=3,
        rubric_type='Group',
        category='Presentation',
        pbl_lvl='PBL2'
    )
    db.session.add(temp)

    db.session.commit()

def populate_gradesheet():
    rubric = Rubric.query.all()
    new_template = Template(sheet_type='Individual')
    new_template.rubric.append(rubric[0])
    new_template.rubric.append(rubric[1])
    new_template.rubric.append(rubric[2])
    new_template.rubric.append(rubric[3])
    new_template.rubric.append(rubric[4])
    db.session.add(new_template)


    new_template = Template(sheet_type='Group')
    new_template.rubric.append(rubric[5])
    new_template.rubric.append(rubric[6])
    new_template.rubric.append(rubric[7])
    db.session.add(new_template)
    
    new_template = Template(sheet_type='Group')
    new_template.rubric.append(rubric[8])
    new_template.rubric.append(rubric[9])
    new_template.rubric.append(rubric[10])
    new_template.rubric.append(rubric[11])
    new_template.rubric.append(rubric[12])
    new_template.rubric.append(rubric[13])
    new_template.rubric.append(rubric[14])
    new_template.rubric.append(rubric[15])
    new_template.rubric.append(rubric[16])
    new_template.rubric.append(rubric[17])
    new_template.rubric.append(rubric[18])
    new_template.rubric.append(rubric[19])
    new_template.rubric.append(rubric[20])
    db.session.add(new_template)

    db.session.commit()