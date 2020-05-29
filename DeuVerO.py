import os
import re
import random


 
def index_check(str, file):
    map = {
        "VT":1, "VI":2, "VR":3, "VIT":4, "VIR":5, "VTR":6, \
        "VITR":7, "noun":8, "adj":9, "adv":10, "other":11
    }
    i = map.get(str, 0)
    if i == 0:
        return False; 
    elif i >= 1 and i <= 7 :
        verb.writing(file, str)
    elif i == 8 :
        noun.writing(file)
    elif i == 9 :
        adj.writing(file)
    elif i == 10 :
        adv.writing(file)
    elif i == 11 :
        other.writing(file)
    return True
        
def check_correctness(arg_1, *arg_2):
    
    print(arg_1)
    for arg in arg_2:
        print(arg);
    
    print("Is the following data correct? (Y/n)")
    if(input() != "" ):
        return  False
    else:
        return  True
        
def writing_file(file, arg_1, *arg_2):
    file.write(arg_1 + '\n')
    for arg in arg_2:
        if type(arg) != list:
            file.write(arg)
        else:
            for i in arg:
                file.write(i + '\t');
        file.write('\n')    
        

def Writing_work(filename):

    with open("./" + filename, 'a' , encoding='UTF-8') as file:

        clear_level = False;
        while (not clear_level):
            part_of_speech = input("Input the part of speech of the word:");
            part_of_speech.lower();
            if not index_check(part_of_speech, file) :
                print("error, please input \"VT\", \"VI\", \"VR\", \"noun\", \"adj\", \"adv\" or \"other\". ");
            else:
                clear_level = True;
    

        clear_level_3 = False
        while(not clear_level_3):
            num_ex = input("Input the num of example:")
            if not (num_ex.isdigit() & (len(num_ex) == 1)):
                print("please input a number < 10.")
                continue
            
            num = int(num_ex)
            for i in range(0, num):
                m_ex = input("Input the meaning of example sentence:\n")
                ex = input("Input the example sentence:\n")
                if check_correctness(m_ex, ex):
                    clear_level_3 = True
                    writing_file(file, m_ex, ex)

class _word_:
    word_meaning = ""
    example_meaning = []
    example = []
    
    def __init__(self, word_meaning, example_meaning, example):
        self.word_meaning = word_meaning
        self.example_meaning = example_meaning
        self.example = example
        
    def read_word_meaning(self):
        return self.word_meaning
    
    def read_example_meaning(self):
        return self.example_meaning
        
    def read_example(self):
        return self.example
        
class noun(_word_):
    word_genus = ""
    word_single = ""
    word_plural = ""
    
    def __init__(self, word_meaning, word_genus, word_single, word_plural, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word_genus = word_genus
        self.word_single = word_single
        self.word_plural = word_plural
        
    def read_word(self):
        return [self.word_genus, self.word_single, self.word_plural]
        
    @staticmethod
    def noun_writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("N: Input the meaning of the word:")
            form = [input("N: Input the single form of the noun:"), input("N: Input the plural form of the noun:")]
            if check_correctness(meaning, form):
                clear_level_2 = True
                print("noun")
                writing_file(file, "//noun", meaning, form)
    
class verb(_word_):
    word_0_form = ""
    word_1_form = ""
    word_p_form = ""
    verb_type = ""
    synonym = []
    antonym = []
    
    def __init__(self, verb_type, word_meaning, synonym, antonym, word_0_form, word_1_form, word_p_form, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word_0_form = word_0_form
        self.word_1_form = word_1_form
        self.word_p_form = word_p_form
        self.verb_type = verb_type
        self.synonym = synonym
        self.antonym = antonym
    
    def read_word(self):
        return [self.word_0_form, self.word_1_form, self.word_p_form]
    
    def read_synonym(self):
        return self.synonym
        
    def read_antonym(self):
        return self.antonym
        
    def read_type(self):
        return self.verb_type
    
    @staticmethod
    def writing(file, _verb_type):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("V: Input the meaning of the word:")
            conjugation = [input("V: Input the origin form of the verb:"), input("V: Input the Präteritum form of the verb:"),\
            input("V: Input the perfekt form of the verb:")]
            if check_correctness(meaning, conjugation):
                clear_level_2 = True
                writing_file(file, "//" + _verb_type, meaning, conjugation )


class adj(_word_):
    word = ""
    
    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
        
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Adj: Input the meaning of the word:")
            form =  input("Adj: Input the adj:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//adj", meaning, form)
        
class adv(_word_):
    word = ""

    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
    
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Adv: Input the meaning of the word:")
            form =  input("Adv: Input the adv:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//adv", meaning, form)

class other(_word_):
    word = ""

    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
        
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Other: Input the meaning of the word:")
            form =  input("Other: Input the word:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//other", meaning, form)
    
def Reading_work(char, word_list):
    
    
    word_count = 0
    with open("./" + char , 'r' , encoding='UTF-8') as file:
        
        word_list[char] = []
        content = file.readlines()
        content = [x.strip() for x in content] 
        
        for i in range(0, len(content)):
            
            print(content[i])
            data = content[i].split()
            if(data[0].find('/',0,2) != -1):
                word_count += 1
                data[0] = data[0].strip('/')
                #if (i + 5) > len(content):
                    #print("Reading ./" + char + ".Word on line " + i + " Error! Check the file format.")
                    #break
                if(data[0] == "noun"):
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    data = content[i].split()
                    #print(data)
                    word_genus = ""
                    word_single = ""
                    word_plural = ""
                    if(len(data) == 1):
                        word_single = data[0]
                    elif(len(data) == 2):
                        word_genus = data[0]
                        word_single = data[1]
                    elif(len(data) >= 3):
                        word_genus = data[0]
                        word_single = data[1]
                        word_plural = data[2]
                    i += 1
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2
                        
                    word_list[char].append(noun(word_meaning, word_genus, word_single,\
                    word_plural, example_meaning, example))
                    
                elif(Ver_type.count(data[0]) != 0):
                    
                    verb_type = data[0]
                    
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    data = content[i].split()
                    if(len(data) < 3 ):
                        print("readfile error! please check for 3 form of verb!")
                    word_0_form = data[0]
                    word_1_form = data[1]
                    word_p_form = data[2]
                    i += 1
                    data = content[i].split()
                    synonym = []
                    antonym = []
                    while(data[0] == "<->" or data[0] == "=" ):
                        if(data[0] == "="):
                            for x in range(1, len(data)):
                                synonym.append(data[x])
                        elif(data[0] == "<->"):
                            for x in range(1, len(data)):
                                antonym.append(data[x])
                        i += 1
                        data = content[i].split()
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2
                    
                    word_list[char].append(verb(verb_type, word_meaning, synonym, antonym, \
                    word_0_form, word_1_form, word_p_form, example_meaning, example))
                
                else:
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    word = content[i]
                    i += 1
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2 
                    
                    if(data[0] == "adj"):
                        word_list[char].append(adj(word_meaning, word, example_meaning, example))
                    elif(data[0] == "adv"):
                        word_list[char].append(adv(word_meaning, word, example_meaning, example))
                    elif(data[0] == "other"):
                        word_list[char].append(other(word_meaning, word, example_meaning, example))
                    else:
                        raise NameError('Error Word Specified')
    
    return word_count
            
def Decoding_word(origin_str, str = ""):
    rnds = [random.randint(0, len(origin_str)-1) for _ in range(0, int(format(len(origin_str)*0.25,'.0f')))]
    #print(rnds)
    new_str = []
    
    for i in range(0, len(origin_str)):
        if(origin_str[i] == " "):
            new_str.append(" ")
            continue
        if(str == ""):
            new_str.append("_")
        else:
            new_str.append(str[i])
    
    for j in rnds:
        new_str[j] = origin_str[j]
    
    string_ = ""
    for k in new_str:
        string_ += k
    
    return string_
    
def example_sentence_test(word):
    j = 0
    for i in word.read_example_meaning():
        answer = input("Input the word example of \"" + i + "\".\n")
        
        True_word = word.read_example()[j]
        word_Hint = ""
        clear_level_2 = False
        while not clear_level_2:
            if answer == (word.read_example()[j]):
                print("Well done~\n")
                clear_level_2 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_example()[j])
                clear_level_2 = True
            else:
                word_Hint = Decoding_word(True_word, word_Hint)
                answer = input( "Incorrect. Try again.\nHint: {0} \n".format(word_Hint)  )
        j += 1

def checking_answer(word):

    answer = input("Input the word means \"" + word.read_word_meaning() + "\".\n")
    if type(word) == noun:
        clear_level_1 = False
        while not clear_level_1:
            if answer == (word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2]):
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2])
                clear_level_1 = True
            else:
                answer = input("If the word are noun, input genus single plural form and separated them by a space.\n")
                
        example_sentence_test(word)
    
    elif type(word) == verb:
        clear_level_1 = False
        
        str_tmp = ""
        for i in word.read_synonym():
            str_tmp += i + " "
        if(str_tmp != ""):
            print("synonym: \n"+ str_tmp)
        str_tmp = ""
        for i in word.read_antonym():
            str_tmp += i + " "
        if(str_tmp != ""):
            print("antonym: \n"+ str_tmp + "\n")
        
        while not clear_level_1:
            if answer == (word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2]):
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2] )
                clear_level_1 = True
            else:
                answer = input("If the word are verb, input origin, Präteritum third person and perfekt form and separated them by a space.\n")
                
        example_sentence_test(word)
            
    else:
        clear_level_1 = False
        while not clear_level_1:
            if answer == word.read_word():
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word())
                clear_level_1 = True
            else:
                answer = input("Incorrect! try again.\n")
                
        example_sentence_test(word)
        
def Testing_work(word_list):

    while True:
        testing_time = input("How many times do you want to test?")
        intmp = input("Specify the verb to test. Enter if no specified character.")
        spec_char = intmp.split()
        
        if(testing_time.isdigit()):
            if(int(testing_time) == 0):
                break
                
            for i in range(0, int(testing_time)):
                while True:
                    if len(spec_char) == 0:
                        char = ""
                        num = random.randint(1, word_num)
                        for i in list(word_list):
                            if(num > len(word_list[i])):
                                num = num - len(word_list[i])
                            else:
                                char = i
                    else:
                        char = random.choice(spec_char)
                    #print(char)
                    #print(i)
                    if(word_list.get(char, '') != ''):
                        index = random.randint(0,len(word_list[char])-1)
                        
                        checking_answer(word_list[char][index])
                        break
                    #if we can't find the char file, continue until we found that.
                    else:
                        check_validity = False
                        for j in spec_char:
                            if(word_list.get(j, '') != ''):
                                check_validity = True
                                break
                            
                        if not check_validity:
                            print("Error input! no such file!")
                            break
                
                #print(i)
                
        else:
            print("Input a number.\n")
            continue
        
    print("Testing Finish!")            

def Output_work(word_list, outputfile_name = "./Word_Card.txt", key_list = [] ):
    
    with open(outputfile_name, 'w' , encoding='UTF-8') as file:
        #key_list is the output key in word_list, if it's empty, then output all keys as default.
        if not key_list:
            key_list = word_list.keys()
        for key in key_list:
        
            for word in word_list[key]:
                output = ""
                output += word.read_word_meaning() + '\t'
                if type(word) == noun:
                    
                    if(word.read_word()[0] != "" and word.read_word()[2] != ""):
                        output += word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2] + '\t'
                    elif (word.read_word()[0] != "" and word.read_word()[2] == ""):
                        output += word.read_word()[0] + " " + word.read_word()[1] + '\t'
                    else:
                        output += word.read_word()[2] + '\t'
                        
                    #j = 0
                    #for i in word.read_example_meaning():
                    #    if(j >= 4):
                    #        break
                    #    output += i + '\t'
                    #    output += word.read_example()[j] + '\t'
                    #    
                    #    j += 1
                    
                    output = output.strip()
                    #while(j < 4):
                    #    output += ' ' + '\t' + ' ' + '\t'
                    #    j += 1
                
                elif type(word) == verb:
                
                    output += word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2] + '\t'
                    
                    #j = 0
                    #for i in word.read_example_meaning():
                    #    if(j >= 4):
                    #        break
                    #    output += i + '\t'
                    #    output += word.read_example()[j] + '\t'
                    #    
                    #    j += 1
                    
                    output = output.strip()
                    #while(j < 4):
                    #    output += ' ' + '\t' + ' ' + '\t'
                    #    j += 1
                        
                else:
                    output += word.read_word() + '\t'
                    
                    #j = 0
                    #for i in word.read_example_meaning():
                    #    if(j >= 4):
                    #        break
                    #    output += i + '\t'
                    #    output += word.read_example()[j] + '\t'
                    #    
                    #    j += 1
                        
                    output = output.strip()
                    #while(j < 4):
                    #    output += ' ' + '\t' + ' ' + '\t'
                    #    j += 1
                
                output += '\n'
                file.write(output)


def Selection_work(word_list, selection):
    global State_clear
    
    if(selection == "prefix"):
        Prefix_construction(word_list, prefix_list)
        return State_clear.append(selection)
    elif(selection == "syn&antonym"):
        #Syn_antonym_construction(word_list, )
        return State_clear.append(selection)
        
    for key in word_list.keys():
        
        for word in word_list[key]:
            if(type(word) != verb):
                continue
            if(selection == "VI"):
                if(word.read_type() == "VI" or word.read_type() == "VIR" or word.read_type() == "VIT" or word.read_type() == "VITR"):
                    select_list["VI"].append(word)
                    
            elif(selection == "VR"):
                if(word.read_type() == "VR" or word.read_type() == "VIR" or word.read_type() == "VTR" or word.read_type() == "VITR"):
                    select_list["VR"].append(word)
                    
            elif(selection == "sein"):
                text = word.read_word_meaning()
                if(text.count("sein") != 0):
                    select_list["sein"].append(word)
                    
    State_clear.append(selection)

def Prefix_construction(word_list, prefix_list):
    global prefix
    
    for key in prefix:
        prefix_list[key] = []
    
    for key in word_list.keys():
        
        for word in word_list[key]:
            if(type(word) != verb):
                continue
            origin_form = word.read_word()[0]
            if not origin_form.endswith(key):
                raise RuntimeError("an exception of string endswith occur!")
            word_prefix = origin_form.replace(key, "", 1)
            
            if not word_prefix in prefix_list:
                print("prefix error! no prefix " + word_prefix + " in file " + key)
            prefix_list[word_prefix].append(word)

    op = input("Do you want to output file?(Y/n)\n")
    if(op == "Y"):
        if not os.path.isdir("./prefix"):
            os.makedirs("./prefix")
        for key in prefix:
            Output_work(prefix_list, "./prefix/" + key + ".txt" , [key])

def Query_RE_work(word_list, q_str, position, output_or_not = False):
    
    pattern = re.compile(q_str)
    
    result_list = []
    bytes_tabtrans = bytes.maketrans(b'/\:?"*<|>', b'ABCDEFGHI')
    
    for key in word_list.keys():
        
        for word in word_list[key]:
            find_list = []
            word_re_list = []
            
            word_o = word.read_word()
            word_m = word.read_word_meaning()
            word_ex_o = word.read_example()
            word_ex_m = word.read_example_meaning()
            
            
            for exo in word_ex_o:
                find_list.extend(pattern.findall(exo))
            for exm in word_ex_m:
                find_list.extend(pattern.findall(exm))
            
            for wo in word_o:
                word_re_list.extend(pattern.findall(wo))
                
            if(position == "1"):
                if (len(pattern.findall(word_m)) != 0):
                    result_list.append(word)
            elif(position == "2"):
                if (len(word_re_list) != 0):
                    result_list.append(word)
            elif(position == "3"):
                if (len(find_list) != 0):
                    result_list.append(word)
            elif(position == "4"):
                if (len(find_list) + len(pattern.findall(word_m)) + len(word_re_list) != 0):
                    result_list.append(word)     
    
    if(output_or_not):
        output_list = {q_str: result_list}
        if not os.path.isdir("./query"):
            os.makedirs("./query")
        
        return Output_work(output_list, "./query/" + q_str.translate(bytes_tabtrans) + ".txt", [q_str])
    else:
        return result_list
    
def Query_work(word_list, q_str, position, output_or_not = False):
    
    result_list = []
    bytes_tabtrans = bytes.maketrans(b'/\:?"*<|>', b'ABCDEFGHI')
    
    
    for key in word_list.keys():
        
        for word in word_list[key]:
            total_count = 0
            word_count = 0
            
            word_o = word.read_word()
            word_m = word.read_word_meaning()
            word_ex_o = word.read_example()
            word_ex_m = word.read_example_meaning()
            
            for exo in word_ex_o:
                total_count += exo.count(q_str)
            for exm in word_ex_m:
                total_count += exm.count(q_str)
            
            for wo in word_o:
                word_count += wo.count(q_str)
                
            if(position == "1"):
                if (word_m.count(q_str)!= 0):
                    result_list.append(word)
            elif(position == "2"):
                if (word_count != 0):
                    result_list.append(word)
            elif(position == "3"):
                if (total_count != 0):
                    result_list.append(word)
            elif(position == "4"):
                if (total_count + word_m.count(q_str) + word_count != 0):
                    result_list.append(word)     
    
    if(output_or_not):
        output_list = {q_str: result_list}
        if not os.path.isdir("./query"):
            os.makedirs("./query")
        
        return Output_work(output_list, "./query/" + q_str.translate(bytes_tabtrans) + ".txt", [q_str])
    else:
        return result_list
    
def work_check(str):
    map = {
        "w":1, "t":2, "q":3, "e":4, "o":5, "s":6
    }
    i = map.get(str, 0)
    if i == 0:
        return False; 
    else:
        return True

select_list = {"VI":[], "VR":[], "sein":[], "prefix":[], "syn&antonym":[], "plus":[]}
prefix_list = {"":[]}
word_list = {"":[]}
#syn_ant_list = {"":[]}
read_clear = False
word_num = 0
State_clear = []
Ver_type = ["VI", "VT", "VR", "VIT", "VIR", "VTR", "VITR"]
prefix = ["ab", "abbe", "an", "auf", "aufrechter", "aus", "auseinander", "be", \
          "beauf", "beg", "bei", "bekannt", "bereit", "bevor", "bewusst", "durch", \
          "ein", "einbe", "er", "ernst", "emp", "ent", "entgegen", "fern", "fertig", \
          "fest", "fort", "frei", "ge", "geheim", "heim", "her", "herab", "herauf", \
          "heraus", "hervor", "hin", "hinter", "kaputt", "klar", "klein", "leicht", \
          "leid", "los", "miss", "mit", "mitbe", "nach", "nahe", "nieder", "offen", \
          "schwer", "sicher", "sitzen", "stehen", "teil", "über", "überein", "übrig", \
          "um", "unter", "ver", "voll", "vor", "voran", "voraus", "vorbei", "vorher", \
          "weg", "weh", "wider", "wieder", "zer", "zu", "zurecht", "zurück", "zusammen"]
         
file_n = ["AB", "BB", "BD", "DF", "FF", "F2", "FG", "GH", "HH", "HK", "KL",\
          "LL", "LM", "MN", "NP", \
          "PR", "RS", "SS", "S2", "S3", "S4", "S5", "ST", "TW", "WW", "WZ"]

while(True):
    work_clear = False
    
    while(not work_clear):
        work = input("Input the work to do.\n")
        if not work_check(work):
            print("error, please input \"w\", \"s\", \"t\", \"o\" or \"q\". Or \"e\" to exit.")
        else:
            work_clear = True

    if work == 'w':
        work_clear_2 = False
        character = ''
    
        while(not work_clear_2):
            character = input("Which verb do you want to write?")
            if(character.isalpha() ):
                work_clear_2 = True
            else:
                print("error , please input one verb")
        
        Writing_work(character)
        
    elif work == 't':
        
        file_name = ''
        while(not read_clear):
            for file_name in file_n:
                
                if(file_name == file_n[-1]):
                    read_clear = True
        
                if not os.path.isfile("./" + file_name):
                    print("no " + tiger + ".Word file!")
                    continue
                word_num += Reading_work(file_name, word_list)
                
                
        print("Total word: ")
        print(word_num)
        Testing_work(word_list)
        
    elif work == 'q':
    
        file_name = ''
        while(not read_clear):
            for file_name in file_n:
                
                if(file_name == file_n[-1]):
                    read_clear = True
        
                if not os.path.isfile("./" + file_name):
                    print("no " + tiger + ".Word file!")
                    continue
                word_num += Reading_work(file_name, word_list)
                
        print("Total word: ")
        print(word_num)
        
        
        while(True):
            query_pos = input("Input the query position. 1:word_meaning 2:word 3:sentence 4:all\n")
            if(query_pos != "1" and query_pos != "2" and query_pos != "3" and query_pos != "4"):
                print("error input!\n")
            else:
                break
        
        RE_or_not = input("Do you want to query by using regular expression?(Y/n)\n")

        q_str = input("Input the query string.\n")
        
        op = input("Do you want to output file?(Y/n)\n")
        
        if(RE_or_not == "Y"):
            if(op == "Y"):
                Query_RE_work(word_list, q_str, query_pos, True)
            else:
                Query_RE_work(word_list, q_str, query_pos, False)
        else:
            if(op == "Y"):
                Query_work(word_list, q_str, query_pos, True)
            else:
                Query_work(word_list, q_str, query_pos, False)
        
    elif work == 'o':
    
        file_name = ''
        while(not read_clear):
            for file_name in file_n:
                
                if(file_name == file_n[-1]):
                    read_clear = True
        
                if not os.path.isfile("./" + file_name):
                    print("no " + tiger + ".Word file!")
                    continue
                word_num += Reading_work(file_name, word_list)
                
        print("Total word: ")
        print(word_num)
        
        Output_work(word_list)
    
    elif work == 's':
    
        file_name = ''
        while(not read_clear):
            for file_name in file_n:
                
                if(file_name == file_n[-1]):
                    read_clear = True
        
                if not os.path.isfile("./" + file_name):
                    print("no " + tiger + ".Word file!")
                    continue
                word_num += Reading_work(file_name, word_list)
                
        print("Total word: ")
        print(word_num)
        
        output_file_YN = False
        work_clear = False
        selection_mode = {
                "VI":1, "VR":2, "sein":3, "prefix":4, "syn&antonym":5
        } 
        while(not work_clear):
            selection = input("Input the selection condition.\nYou have following choice:\nVI, VR, sein, prefix, syn&antonym\n")
            if(selection_mode.get(selection, 0) == 0):
                print("selection error, try again")
            else:
                work_clear = True
        
        if(State_clear.count(selection) != 0):
            print(selection + " has been done!")
            continue
        Selection_work(word_list, selection)
        
        if(selection_mode.get(selection, 0) < 4 ):
            op = input("Do you want to output file?(Y/n)\n")
            if(op == "Y"):
                Output_work(select_list, selection + ".txt", [selection])
            
            
        
    elif work == 'e':
        break
    
    

    

