import os
import argparse
import shutil
def load_dir(path,Extension=None):
    '''
        input : dir(path,Extension)
        ex : dirpath, txt or jpg....
        retrun dir list(path+filename)
    '''
    l=[]
    for i in os.listdir(path):
        if Extension!=None:
            if i.endswith(Extension):                
                l.append(os.path.join(path,i))
        else:
            l.append(os.path.joing(path,i))
    return l
def reanme(old):
    '''
        input : old name(path)
            os.reanme(old,new)
        output : new name
    '''
    return 'finish'
    
def moveto(filepath:list,dir,dir_name='output'):
    '''
        input : path 
    '''
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    move_dir=os.path.join(dir,dir_name)
    for i in filepath:
        shutil.move(i,move_dir)
    return 'finish'




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ext', type=str)
    opt = parser.parse_args()
    path = os.getcwd()
    ext = opt.ext
    l = load_dir(path,ext)
    moveto(l,path,dir_name=ext)

