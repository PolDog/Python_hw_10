import pandas as pd
import random
def print_df(text,data):
    print(f'========= {text} =================')
    print(data.head(20))

def create_get_dummies(data):
    data=pd.get_dummies(data['whoAmI'])
    print_df('get_dummies ',data)

def my_method(data):
    original_list=data['whoAmI'].tolist()
    human_id=[]
    robot_id=[]
    for i in range(len(original_list)):
        if original_list[i]=='human':
            human_id.append('True')
            robot_id.append('False')
        else:
            human_id.append('False')
            robot_id.append('True')
    data2={'Human':human_id,'robot':robot_id}
    one_hot=pd.DataFrame(data2)
    print_df('one hot',one_hot)

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print_df('оригинал',data)
create_get_dummies(data)
my_method(data)
