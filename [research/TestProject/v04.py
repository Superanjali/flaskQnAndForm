# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 08:47:59 2018

@author: User
"""

from __future__ import print_function
import json
from watson_developer_cloud import AssistantV1
import csv

# Parameters ####################################
param_username = 'bd8cc8ab-442f-40c9-8c27-e2835b7d3745'
param_password = '6o4z02ADfI0z'
param_workspace_id = 'd08163fc-41bd-433a-b3a2-a31bda4491ab'

# Functions #####################################

def readExamples(Qno):
    
    answer = 'input/' + Qno + '_answers.txt'
    wrong = 'input/' + Qno + '_wrong.txt'
    
    with open(answer) as f:
        ans = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    ans = [x.strip() for x in ans if len(x.strip())] 

    csvname = 'input/' + Qno + '.csv'
    with open(csvname,'w') as f:
        for line in ans:
            f.write(line+',yes\n')
    
    with open(wrong) as f:
        wro = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    wro = [x.strip() for x in wro if len(x.strip())] 
    
    with open(csvname,'a') as f:
         for line in wro:
            f.write(line+',no\n')   
    return ans,wro
    

def identify(assistant, workspace_id, answer):
 
    response = assistant.message(
        workspace_id=workspace_id,
        input={
            'text': answer
        })
        
    return [[elem['intent'], elem['confidence']] for elem in response['intents']]


def add_intent(assistant,workspace_id,q1Examples, Q_name):
    examples = [{'text': line} for line in q1Examples]
    response = assistant.create_intent(
        workspace_id=workspace_id,
        intent= Q_name,
        description= 'string',
        examples= examples)
    #print(json.dumps(response, indent=2))
    return json.dumps(response, indent=2)
    
def listWorkspace(assistant):
    response = assistant.list_workspaces()
    #print(json.dumps(response, indent=2))
    res = { x['name']:x['workspace_id'] for x in response['workspaces']}
    return res

def listIntents(assistant,workspace_id):
    response = assistant.list_intents(workspace_id)
    res = {x['intent'] for x in response['intents']}
    return res

# Main code #########################################

class Wat():
    def __init__(self):
        self.assistant = AssistantV1(
                    username= param_username,
                    password=param_password,
                    version='2017-04-21') 

        self.workspace_id = param_workspace_id
        # read question text
        name = 'input\science.csv'
        with open(name, 'r') as f:
            reader = csv.reader(f)
            data = [r for r in reader if r]
        self.qname = {x[0]:x[1] for x in data}    


    def do_stuff(self, inp):
        return_str = ''
        #print('choice:')
        return_str += ''
        line = inp.split()
        text = ' '.join(line[1:])
        user = line[0]
        if user == 'x':
            #print('Exit')
            return_str += 'Exit' + '\n'
            return return_str
            
        elif user == 'c':
            l = listIntents(self.assistant,self.workspace_id)
            if text in l:
                #print('Error intent %s already exists' % text)
                return_str += 'Error intent %s already exists' % text + '\n'
                return return_str
            if text + '_no' in l:
                #print('Error intent %s already exists' % text + '_no')
                return_str += 'Error intent %s already exists' % text + '_no' + '\n'
                return return_str
            #print('Create',line[1:])
            return_str += 'Create' + str(line[1:]) + '\n'
            ans,wrong = readExamples(text) 
           # print(ans,wrong)
            return_str += str(ans) + str(wrong) +'\n'
            add_intent(self.assistant,self.workspace_id,ans,text)
            add_intent(self.assistant,self.workspace_id,wrong,text +'_no')
        elif user == 'd':
            #print('Delete',line[1:])
            return_str += 'Delete' + str(line[1:]) + '\n'
            response = self.assistant.delete_intent(workspace_id=self.workspace_id, intent = text)
            response = self.assistant.delete_intent(workspace_id=self.workspace_id, intent = text + '_no')
        elif user == 'l':
            #print('List',line[1:])
            return_str += 'List' + str(line[1:]) + '\n'
            response = self.assistant.list_intents(workspace_id=self.workspace_id, export=True)
            #print(json.dumps(response, indent=2))
            return_str += json.dumps(response, indent=2) + '\n'
        elif user == 'u':
            #print ('Update',line[1:])
            return_str += 'Update' + str(line[1:]) + '\n'
            response = self.assistant.update_intent(
            workspace_id=self.workspace_id,
            intent= text,
            new_intent='updated_test_intent',
            new_description='Updated test intent.')
            #print(json.dumps(response, indent=2))
            return_str += json.dumps(response, indent=2) + '\n'
        elif user == 'g':
            #print('Get',line[1:])
            return_str += 'Get' + str(line[1:]) + '\n'
            response = self.assistant.get_intent(
                    workspace_id=self.workspace_id, intent= text, export=True)
            #print(json.dumps(response, indent=2))
            return_str += json.dumps(response,indent=2) + '\n'
        elif user == 'a':
            answer = input(self.qname[text]+'\n')
            res = identify(self.assistant, param_workspace_id, answer)
            #print(res)
            return_str += res +'\n' 
            if res and res[0][0] == text and res[0][1] >= 0.7:
                #print('Correct')
                return_str += 'Correct' + '\n'
            else:
                #print('Wrong')
                return_str += 'Wrong' + '\n'
                
        elif user == 't':
            #print('test')
            return_str += 'test' +'\n'
            total = 0
            l = listIntents(self.assistant,self.workspace_id)
            lyes = [x for x in l if x.find('_no') < 0]
            for elem in lyes: 
                #print(self.qname[elem])
                return_str +='\n'
                ans = input()
                res = identify(self.assistant, param_workspace_id, ans)
                #print(res)
                return_str += res +'\n'
                if res and res[0][0] == elem and res[0][1] >= 0.7:
                    #print('Correct')
                    return_str += 'Correct' +'\n'
                    total += (res[0][1] * 100)
                elif res and res[0][0] == elem:
                    #print('Wrong')
                    return_str += 'Wrong' +'\n'
                    total += (res[0][1] * 100)
                else:
                    #print('Wrong') 
                    return_str += 'Wrong' +'\n'
            
            #print('total Score: %.1d out of %d' % (total, len(lyes)*100)) 
            return_str += 'Total Score: %.1d out of %d' % (total,len(lyes)*100) +'\n'
        
        elif user == 'lw':
            res = listWorkspace(self.assistant)
            #print('/n/n'.join([x+':'+res[x] for x in res]))
            return_str += '/n/n'.join([x+':'+res[x] for x in res]) +'\n'
        elif user == 'uw':
            res = listWorkspace(self.assistant)
            if text in res:
                self.workspace_id = res[text]
                #print('Using %s:%s'  % (text,self.workspace_id))
                return_str += 'Using %s:%s' % (text,self.workspace_id) +'\n'
            else:
                #print('Error. Workspace %s is not found' % text)
                return_str += 'Error. Workspace %s in not found' % text +'\n'
        elif user == 'li':
            result = listIntents(self.assistant,self.workspace_id)
            #print(', '.join(result))
            return_str += ', '.join(result) + '\n'
    
        return return_str
    
    def check_answer(self, Qname,ans):
        text = Qname
        answer = ans
        res = identify(self.assistant, param_workspace_id, answer)
        if not res:
            return False, 0
        if res[0][0] != text:
            return False,0        
        if res[0][1] >= 0.7:
            return True , res[0][1]
        else:
            return False, res[0][1]
        