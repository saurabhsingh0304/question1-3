data_dict={
    'dict1':{
        '1':'name1',
        '2':'name2',
        '3':'name3',
        '4':'name4',
    },
    'dict2':{
        '1':30,
        '2':70,
        '3':40,
        '4':60,
    }
}

Keymax = max(data_dict['dict2'], key=data_dict['dict2'].get) 
dic={Keymax:data_dict['dict2'][Keymax]}
print(dic)