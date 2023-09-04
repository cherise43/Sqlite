# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from faker import Faker
# from models import Dev, Company, Freebie, company_dev
# import random
# import ipdb
# creator_engine = create_engine('sqlite:///freebies.db')
# Session = sessionmaker(bind=creator_engine)
# session = Session()

# fake = Faker()


# if __name__ == '__main__':
#     print ("Clearing DB****")
#     session.query(Dev).delete()
#     session.query(Resturant).delete()
#     session.query(Company).delete()
#     print("Done")

#     print("seeding devs....")
#     devs =[]
#     for i in range(10):
#         company=Company(first_name=fake.first_name)
#         session.add(new dev)
#         session.commit()
#         print(***Seeding Done****)
    
#     print("seeding devs")
# print("Now seeding Resturants.............")
# for dev in devs:
#         freebies = [(Freebie(item_name = fake.emoji(), value=fake.random_number(digits=4), dev_id= dev.id, company_id = random.randint(0,9))) for i in range(3)]
#         session.add_all(freebies)
#         session.commit()
# print("*******DEV SEEDING DONE ***********")

# print("Seed Company Devs")
# for i in session.query(Freebie).all():
#         assigned = company_dev.insert().values(dev_id=i.dev_id, company_id=i.company_id)
#         session.execute(assigned)
#         session.commit()
# print("Seed Company Devs Done")

# session.close()