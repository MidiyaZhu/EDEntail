import csv
from random import sample
from numpy import *
'''this is for embedded hypothesis'''
def combine(modifiedfile,savefile):
    rows = []
    with open(modifiedfile) as f:
        csv_read = csv.reader(f)
        for row in csv_read:
            st = []
            st.append(row[0])
            st.append(row[1])
            st.append(row[0] + '</s>' + '</s>' + row[1])
            st.append(row[2])
            st.append(row[3])
            st.append(row[4])
            rows.append(st)
        with open(savefile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(rows)

def mainaman(k):
    datasetnames = [
        'aman'
    ]
    traindev = [
        'train', 'dev',
        'test']

    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 12)
    for dataname in datasetnames:
        if k =='freq':
            hypothesis_emo_syns_LTOS = {
                2: {'noemo': ['others, no emotion'], 'joy': ['gratitude, triumphant'], 'anger': ['hostility, ire'],
                    'sadness': ['sadness, dismal'], 'surprise': ['unforeseen, breathtaking'],
                    'disgust': ['offensive, intolerable'], 'fear': ['horror, shudder']},
                3: {'noemo': ['others, no emotion'], 'joy': ['cheer, bliss, triumphant'],
                    'anger': ['hostility, outrage, discontent'], 'sadness': ['depression, grief, dismal'],
                    'surprise': ['shocked, unbelievable, unforeseen'], 'disgust': ['ugly, offensive, displeasure'],
                    'fear': ['horror, terrifying, suspense']},
                4: {'noemo': ['others, no emotion'], 'joy': ['joy, cheer, bliss, triumphant'],
                    'anger': ['hostility, indignation, outrage, provocation'],
                    'sadness': ['depression, grief, sadness, dismal'],
                    'surprise': ['amazing, shocked, unbelievable, unforeseen'],
                    'disgust': ['bitter, ugly, offensive, nausea'], 'fear': ['horror, terrifying, fright, suspense']},
                5: {'noemo': ['others, no emotion'], 'joy': ['pleasure, achievement, gratitude, cheer, triumphant'],
                    'anger': ['anger, hostility, indignation, aversion, provocation'],
                    'sadness': ['depression, grief, sadness, tragic, blues'],
                    'surprise': ['shock, amazing, shocked, awe, unbelievable'],
                    'disgust': ['bitter, ugly, nausea, aversion, hateful'],
                    'fear': ['horror, panic, insecurity, fright, chilling']}, 6: {'noemo': ['others, no emotion'],
                                                                                  'joy': [
                                                                                      'pleasure, blessed, gratitude, cheer, triumphant, enchantment'],
                                                                                  'anger': [
                                                                                      'fury, hostility, indignation, outrage, aversion, provocation'],
                                                                                  'sadness': [
                                                                                      'grief, sadness, melancholy, sadly, pathetic, dismal'],
                                                                                  'surprise': [
                                                                                      'sudden, shock, amazing, shocked, awe, unbelievable'],
                                                                                  'disgust': [
                                                                                      'ugly, contempt, dislike, nausea, aversion, hateful'],
                                                                                  'fear': [
                                                                                      'worry, horror, panic, terrifying, insecurity, fright']},
                7: {'noemo': ['others, no emotion'],
                    'joy': ['pleasure, achievement, blessed, gratitude, cheer, triumphant, enchantment'],
                    'anger': ['hatred, hostility, indignation, annoyance, aversion, provocation, ire'],
                    'sadness': ['grief, sadness, melancholy, sadly, pathetic, blues, dismal'],
                    'surprise': ['sudden, shock, amazing, shocked, awe, abrupt, startling'],
                    'disgust': ['ugly, contempt, dislike, nausea, vomiting, aversion, hateful'],
                    'fear': ['worry, anxiety, horror, panic, terrifying, insecurity, fright']},
                8: {'noemo': ['others, no emotion'],
                    'joy': ['pleasure, achievement, blessed, cheer, bliss, ecstasy, triumphant, enchantment'],
                    'anger': ['hatred, hostility, indignation, annoyance, aversion, enraged, provocation, ire'],
                    'sadness': ['depression, grief, sadness, melancholy, sadly, pathetic, blues, dismal'],
                    'surprise': ['sudden, shock, curious, amazing, shocked, awe, abrupt, astonishing'],
                    'disgust': ['ugly, offensive, contempt, dislike, nausea, aversion, intolerable, hateful'],
                    'fear': ['worry, anxiety, horror, panic, terrifying, scare, insecurity, fright']},
                9: {'noemo': ['others, no emotion'],
                    'joy': ['pleasure, joy, achievement, blessed, cheer, bliss, ecstasy, triumphant, enchantment'],
                    'anger': [
                        'hatred, fury, resentment, hostility, indignation, outrage, malice, provocation, animosity'],
                    'sadness': ['depression, grief, despair, sadness, melancholy, sadly, pathetic, blues, dismal'],
                    'surprise': ['sudden, shock, curious, amazing, unexpected, awe, abrupt, astonishing, breathtaking'],
                    'disgust': ['ugly, offensive, contempt, dislike, vomiting, disdain, aversion, disgusting, hateful'],
                    'fear': ['worry, anxiety, horror, panic, terrifying, apprehension, scare, insecurity, fright']},
                10: {'noemo': ['others, no emotion'], 'joy': [
                    'pleasure, joy, achievement, blessed, cheer, awesome, bliss, ecstasy, triumphant, enchantment'],
                     'anger': [
                         'rage, hatred, hostility, indignation, annoyance, malice, enraged, provocation, animosity, ire'],
                     'sadness': [
                         'depression, grief, despair, sadness, tragic, melancholy, sadly, pathetic, blues, dismal'],
                     'surprise': [
                         'sudden, shock, curious, amazing, unexpected, awe, unbelievable, unforeseen, breathtaking, perplex'],
                     'disgust': [
                         'ugly, offensive, contempt, dislike, nausea, disdain, aversion, disgusting, intolerable, hateful'],
                     'fear': [
                         'anxiety, horror, panic, terrifying, agitation, apprehension, scare, insecurity, shudder, fright']},
                11: {'noemo': ['others, no emotion'], 'joy': [
                    'pleasure, joy, delight, achievement, blessed, cheer, awesome, bliss, ecstasy, triumphant, enchantment'],
                     'anger': [
                         'anger, rage, hatred, hostility, indignation, annoyance, outrage, malice, enraged, provocation, animosity'],
                     'sadness': [
                         'depression, grief, desperate, despair, sadness, tragic, melancholy, sadly, pathetic, blues, dismal'],
                     'surprise': [
                         'sudden, shock, curious, amazing, dramatic, unexpected, awe, startling, amazingly, breathtaking, perplex'],
                     'disgust': [
                         'ugly, offensive, contempt, disgust, dislike, nausea, disdain, aversion, disgusting, intolerable, hateful'],
                     'fear': [
                         'anxiety, horror, panic, alarm, terrifying, agitation, apprehension, scare, insecurity, shudder, fright']}}
            hypothesis_emo_synspace_LTOS = {
                2: {'noemo': ['others no emotion'], 'joy': ['gratitude triumphant'], 'anger': ['hostility ire'],
                    'sadness': ['sadness dismal'], 'surprise': ['unforeseen breathtaking'],
                    'disgust': ['offensive intolerable'], 'fear': ['horror shudder']},
                3: {'noemo': ['others no emotion'], 'joy': ['cheer bliss triumphant'],
                    'anger': ['hostility outrage discontent'], 'sadness': ['depression grief dismal'],
                    'surprise': ['shocked unbelievable unforeseen'], 'disgust': ['ugly offensive displeasure'],
                    'fear': ['horror terrifying suspense']},
                4: {'noemo': ['others no emotion'], 'joy': ['joy cheer bliss triumphant'],
                    'anger': ['hostility indignation outrage provocation'],
                    'sadness': ['depression grief sadness dismal'],
                    'surprise': ['amazing shocked unbelievable unforeseen'],
                    'disgust': ['bitter ugly offensive nausea'], 'fear': ['horror terrifying fright suspense']},
                5: {'noemo': ['others no emotion'], 'joy': ['pleasure achievement gratitude cheer triumphant'],
                    'anger': ['anger hostility indignation aversion provocation'],
                    'sadness': ['depression grief sadness tragic blues'],
                    'surprise': ['shock amazing shocked awe unbelievable'],
                    'disgust': ['bitter ugly nausea aversion hateful'],
                    'fear': ['horror panic insecurity fright chilling']},
                6: {'noemo': ['others no emotion'], 'joy': ['pleasure blessed gratitude cheer triumphant enchantment'],
                    'anger': ['fury hostility indignation outrage aversion provocation'],
                    'sadness': ['grief sadness melancholy sadly pathetic dismal'],
                    'surprise': ['sudden shock amazing shocked awe unbelievable'],
                    'disgust': ['ugly contempt dislike nausea aversion hateful'],
                    'fear': ['worry horror panic terrifying insecurity fright']}, 7: {'noemo': ['others no emotion'],
                                                                                      'joy': [
                                                                                          'pleasure achievement blessed gratitude cheer triumphant enchantment'],
                                                                                      'anger': [
                                                                                          'hatred hostility indignation annoyance aversion provocation ire'],
                                                                                      'sadness': [
                                                                                          'grief sadness melancholy sadly pathetic blues dismal'],
                                                                                      'surprise': [
                                                                                          'sudden shock amazing shocked awe abrupt startling'],
                                                                                      'disgust': [
                                                                                          'ugly contempt dislike nausea vomiting aversion hateful'],
                                                                                      'fear': [
                                                                                          'worry anxiety horror panic terrifying insecurity fright']},
                8: {'noemo': ['others no emotion'],
                    'joy': ['pleasure achievement blessed cheer bliss ecstasy triumphant enchantment'],
                    'anger': ['hatred hostility indignation annoyance aversion enraged provocation ire'],
                    'sadness': ['depression grief sadness melancholy sadly pathetic blues dismal'],
                    'surprise': ['sudden shock curious amazing shocked awe abrupt astonishing'],
                    'disgust': ['ugly offensive contempt dislike nausea aversion intolerable hateful'],
                    'fear': ['worry anxiety horror panic terrifying scare insecurity fright']},
                9: {'noemo': ['others no emotion'],
                    'joy': ['pleasure joy achievement blessed cheer bliss ecstasy triumphant enchantment'],
                    'anger': ['hatred fury resentment hostility indignation outrage malice provocation animosity'],
                    'sadness': ['depression grief despair sadness melancholy sadly pathetic blues dismal'],
                    'surprise': ['sudden shock curious amazing unexpected awe abrupt astonishing breathtaking'],
                    'disgust': ['ugly offensive contempt dislike vomiting disdain aversion disgusting hateful'],
                    'fear': ['worry anxiety horror panic terrifying apprehension scare insecurity fright']},
                10: {'noemo': ['others no emotion'],
                     'joy': ['pleasure joy achievement blessed cheer awesome bliss ecstasy triumphant enchantment'],
                     'anger': ['rage hatred hostility indignation annoyance malice enraged provocation animosity ire'],
                     'sadness': ['depression grief despair sadness tragic melancholy sadly pathetic blues dismal'],
                     'surprise': [
                         'sudden shock curious amazing unexpected awe unbelievable unforeseen breathtaking perplex'],
                     'disgust': [
                         'ugly offensive contempt dislike nausea disdain aversion disgusting intolerable hateful'],
                     'fear': [
                         'anxiety horror panic terrifying agitation apprehension scare insecurity shudder fright']},
                11: {'noemo': ['others no emotion'], 'joy': [
                    'pleasure joy delight achievement blessed cheer awesome bliss ecstasy triumphant enchantment'],
                     'anger': [
                         'anger rage hatred hostility indignation annoyance outrage malice enraged provocation animosity'],
                     'sadness': [
                         'depression grief desperate despair sadness tragic melancholy sadly pathetic blues dismal'],
                     'surprise': [
                         'sudden shock curious amazing dramatic unexpected awe startling amazingly breathtaking perplex'],
                     'disgust': [
                         'ugly offensive contempt disgust dislike nausea disdain aversion disgusting intolerable hateful'],
                     'fear': [
                         'anxiety horror panic alarm terrifying agitation apprehension scare insecurity shudder fright']}}
            hypothesis_emo_synslash_LTOS = {
                2: {'noemo': ['others/ no emotion'], 'joy': ['gratitude/ triumphant'], 'anger': ['hostility/ ire'],
                    'sadness': ['sadness/ dismal'], 'surprise': ['unforeseen/ breathtaking'],
                    'disgust': ['offensive/ intolerable'], 'fear': ['horror/ shudder']},
                3: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ bliss/ triumphant'],
                    'anger': ['hostility/ outrage/ discontent'], 'sadness': ['depression/ grief/ dismal'],
                    'surprise': ['shocked/ unbelievable/ unforeseen'], 'disgust': ['ugly/ offensive/ displeasure'],
                    'fear': ['horror/ terrifying/ suspense']},
                4: {'noemo': ['others/ no emotion'], 'joy': ['joy/ cheer/ bliss/ triumphant'],
                    'anger': ['hostility/ indignation/ outrage/ provocation'],
                    'sadness': ['depression/ grief/ sadness/ dismal'],
                    'surprise': ['amazing/ shocked/ unbelievable/ unforeseen'],
                    'disgust': ['bitter/ ugly/ offensive/ nausea'], 'fear': ['horror/ terrifying/ fright/ suspense']},
                5: {'noemo': ['others/ no emotion'], 'joy': ['pleasure/ achievement/ gratitude/ cheer/ triumphant'],
                    'anger': ['anger/ hostility/ indignation/ aversion/ provocation'],
                    'sadness': ['depression/ grief/ sadness/ tragic/ blues'],
                    'surprise': ['shock/ amazing/ shocked/ awe/ unbelievable'],
                    'disgust': ['bitter/ ugly/ nausea/ aversion/ hateful'],
                    'fear': ['horror/ panic/ insecurity/ fright/ chilling']}, 6: {'noemo': ['others/ no emotion'],
                                                                                  'joy': [
                                                                                      'pleasure/ blessed/ gratitude/ cheer/ triumphant/ enchantment'],
                                                                                  'anger': [
                                                                                      'fury/ hostility/ indignation/ outrage/ aversion/ provocation'],
                                                                                  'sadness': [
                                                                                      'grief/ sadness/ melancholy/ sadly/ pathetic/ dismal'],
                                                                                  'surprise': [
                                                                                      'sudden/ shock/ amazing/ shocked/ awe/ unbelievable'],
                                                                                  'disgust': [
                                                                                      'ugly/ contempt/ dislike/ nausea/ aversion/ hateful'],
                                                                                  'fear': [
                                                                                      'worry/ horror/ panic/ terrifying/ insecurity/ fright']},
                7: {'noemo': ['others/ no emotion'],
                    'joy': ['pleasure/ achievement/ blessed/ gratitude/ cheer/ triumphant/ enchantment'],
                    'anger': ['hatred/ hostility/ indignation/ annoyance/ aversion/ provocation/ ire'],
                    'sadness': ['grief/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                    'surprise': ['sudden/ shock/ amazing/ shocked/ awe/ abrupt/ startling'],
                    'disgust': ['ugly/ contempt/ dislike/ nausea/ vomiting/ aversion/ hateful'],
                    'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ insecurity/ fright']},
                8: {'noemo': ['others/ no emotion'],
                    'joy': ['pleasure/ achievement/ blessed/ cheer/ bliss/ ecstasy/ triumphant/ enchantment'],
                    'anger': ['hatred/ hostility/ indignation/ annoyance/ aversion/ enraged/ provocation/ ire'],
                    'sadness': ['depression/ grief/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                    'surprise': ['sudden/ shock/ curious/ amazing/ shocked/ awe/ abrupt/ astonishing'],
                    'disgust': ['ugly/ offensive/ contempt/ dislike/ nausea/ aversion/ intolerable/ hateful'],
                    'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ scare/ insecurity/ fright']},
                9: {'noemo': ['others/ no emotion'],
                    'joy': ['pleasure/ joy/ achievement/ blessed/ cheer/ bliss/ ecstasy/ triumphant/ enchantment'],
                    'anger': [
                        'hatred/ fury/ resentment/ hostility/ indignation/ outrage/ malice/ provocation/ animosity'],
                    'sadness': ['depression/ grief/ despair/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                    'surprise': ['sudden/ shock/ curious/ amazing/ unexpected/ awe/ abrupt/ astonishing/ breathtaking'],
                    'disgust': ['ugly/ offensive/ contempt/ dislike/ vomiting/ disdain/ aversion/ disgusting/ hateful'],
                    'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ apprehension/ scare/ insecurity/ fright']},
                10: {'noemo': ['others/ no emotion'], 'joy': [
                    'pleasure/ joy/ achievement/ blessed/ cheer/ awesome/ bliss/ ecstasy/ triumphant/ enchantment'],
                     'anger': [
                         'rage/ hatred/ hostility/ indignation/ annoyance/ malice/ enraged/ provocation/ animosity/ ire'],
                     'sadness': [
                         'depression/ grief/ despair/ sadness/ tragic/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                     'surprise': [
                         'sudden/ shock/ curious/ amazing/ unexpected/ awe/ unbelievable/ unforeseen/ breathtaking/ perplex'],
                     'disgust': [
                         'ugly/ offensive/ contempt/ dislike/ nausea/ disdain/ aversion/ disgusting/ intolerable/ hateful'],
                     'fear': [
                         'anxiety/ horror/ panic/ terrifying/ agitation/ apprehension/ scare/ insecurity/ shudder/ fright']},
                11: {'noemo': ['others/ no emotion'], 'joy': [
                    'pleasure/ joy/ delight/ achievement/ blessed/ cheer/ awesome/ bliss/ ecstasy/ triumphant/ enchantment'],
                     'anger': [
                         'anger/ rage/ hatred/ hostility/ indignation/ annoyance/ outrage/ malice/ enraged/ provocation/ animosity'],
                     'sadness': [
                         'depression/ grief/ desperate/ despair/ sadness/ tragic/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                     'surprise': [
                         'sudden/ shock/ curious/ amazing/ dramatic/ unexpected/ awe/ startling/ amazingly/ breathtaking/ perplex'],
                     'disgust': [
                         'ugly/ offensive/ contempt/ disgust/ dislike/ nausea/ disdain/ aversion/ disgusting/ intolerable/ hateful'],
                     'fear': [
                         'anxiety/ horror/ panic/ alarm/ terrifying/ agitation/ apprehension/ scare/ insecurity/ shudder/ fright']}}
            hypothesis_emo_synsand_LTOS = {
                2: {'noemo': ['others and no emotion'], 'joy': ['gratitude and triumphant'],
                                             'anger': ['hostility and ire'], 'sadness': ['sadness and dismal'],
                                             'surprise': ['unforeseen and breathtaking'],
                                             'disgust': ['offensive and intolerable'], 'fear': ['horror and shudder']},
                                         3: {'noemo': ['others and no emotion'],
                                             'joy': ['cheer and bliss and triumphant'],
                                             'anger': ['hostility and outrage and discontent'],
                                             'sadness': ['depression and grief and dismal'],
                                             'surprise': ['shocked and unbelievable and unforeseen'],
                                             'disgust': ['ugly and offensive and displeasure'],
                                             'fear': ['horror and terrifying and suspense']},
                                         4: {'noemo': ['others and no emotion'],
                                             'joy': ['joy and cheer and bliss and triumphant'],
                                             'anger': ['hostility and indignation and outrage and provocation'],
                                             'sadness': ['depression and grief and sadness and dismal'],
                                             'surprise': ['amazing and shocked and unbelievable and unforeseen'],
                                             'disgust': ['bitter and ugly and offensive and nausea'],
                                             'fear': ['horror and terrifying and fright and suspense']},
                                         5: {'noemo': ['others and no emotion'],
                                             'joy': ['pleasure and achievement and gratitude and cheer and triumphant'],
                                             'anger': [
                                                 'anger and hostility and indignation and aversion and provocation'],
                                             'sadness': ['depression and grief and sadness and tragic and blues'],
                                             'surprise': ['shock and amazing and shocked and awe and unbelievable'],
                                             'disgust': ['bitter and ugly and nausea and aversion and hateful'],
                                             'fear': ['horror and panic and insecurity and fright and chilling']},
                                         6: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and blessed and gratitude and cheer and triumphant and enchantment'],
                                             'anger': [
                                                 'fury and hostility and indignation and outrage and aversion and provocation'],
                                             'sadness': [
                                                 'grief and sadness and melancholy and sadly and pathetic and dismal'],
                                             'surprise': [
                                                 'sudden and shock and amazing and shocked and awe and unbelievable'],
                                             'disgust': [
                                                 'ugly and contempt and dislike and nausea and aversion and hateful'],
                                             'fear': [
                                                 'worry and horror and panic and terrifying and insecurity and fright']},
                                         7: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and achievement and blessed and gratitude and cheer and triumphant and enchantment'],
                                             'anger': [
                                                 'hatred and hostility and indignation and annoyance and aversion and provocation and ire'],
                                             'sadness': [
                                                 'grief and sadness and melancholy and sadly and pathetic and blues and dismal'],
                                             'surprise': [
                                                 'sudden and shock and amazing and shocked and awe and abrupt and startling'],
                                             'disgust': [
                                                 'ugly and contempt and dislike and nausea and vomiting and aversion and hateful'],
                                             'fear': [
                                                 'worry and anxiety and horror and panic and terrifying and insecurity and fright']},
                                         8: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and achievement and blessed and cheer and bliss and ecstasy and triumphant and enchantment'],
                                             'anger': [
                                                 'hatred and hostility and indignation and annoyance and aversion and enraged and provocation and ire'],
                                             'sadness': [
                                                 'depression and grief and sadness and melancholy and sadly and pathetic and blues and dismal'],
                                             'surprise': [
                                                 'sudden and shock and curious and amazing and shocked and awe and abrupt and astonishing'],
                                             'disgust': [
                                                 'ugly and offensive and contempt and dislike and nausea and aversion and intolerable and hateful'],
                                             'fear': [
                                                 'worry and anxiety and horror and panic and terrifying and scare and insecurity and fright']},
                                         9: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and joy and achievement and blessed and cheer and bliss and ecstasy and triumphant and enchantment'],
                                             'anger': [
                                                 'hatred and fury and resentment and hostility and indignation and outrage and malice and provocation and animosity'],
                                             'sadness': [
                                                 'depression and grief and despair and sadness and melancholy and sadly and pathetic and blues and dismal'],
                                             'surprise': [
                                                 'sudden and shock and curious and amazing and unexpected and awe and abrupt and astonishing and breathtaking'],
                                             'disgust': [
                                                 'ugly and offensive and contempt and dislike and vomiting and disdain and aversion and disgusting and hateful'],
                                             'fear': [
                                                 'worry and anxiety and horror and panic and terrifying and apprehension and scare and insecurity and fright']},
                                         10: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and joy and achievement and blessed and cheer and awesome and bliss and ecstasy and triumphant and enchantment'],
                                              'anger': [
                                                  'rage and hatred and hostility and indignation and annoyance and malice and enraged and provocation and animosity and ire'],
                                              'sadness': [
                                                  'depression and grief and despair and sadness and tragic and melancholy and sadly and pathetic and blues and dismal'],
                                              'surprise': [
                                                  'sudden and shock and curious and amazing and unexpected and awe and unbelievable and unforeseen and breathtaking and perplex'],
                                              'disgust': [
                                                  'ugly and offensive and contempt and dislike and nausea and disdain and aversion and disgusting and intolerable and hateful'],
                                              'fear': [
                                                  'anxiety and horror and panic and terrifying and agitation and apprehension and scare and insecurity and shudder and fright']},
                                         11: {'noemo': ['others and no emotion'], 'joy': [
                                             'pleasure and joy and delight and achievement and blessed and cheer and awesome and bliss and ecstasy and triumphant and enchantment'],
                                              'anger': [
                                                  'anger and rage and hatred and hostility and indignation and annoyance and outrage and malice and enraged and provocation and animosity'],
                                              'sadness': [
                                                  'depression and grief and desperate and despair and sadness and tragic and melancholy and sadly and pathetic and blues and dismal'],
                                              'surprise': [
                                                  'sudden and shock and curious and amazing and dramatic and unexpected and awe and startling and amazingly and breathtaking and perplex'],
                                              'disgust': [
                                                  'ugly and offensive and contempt and disgust and dislike and nausea and disdain and aversion and disgusting and intolerable and hateful'],
                                              'fear': [
                                                  'anxiety and horror and panic and alarm and terrifying and agitation and apprehension and scare and insecurity and shudder and fright']}}
        else:
            hypothesis_emo_syns_LTOS = {
                2: {'noemo': ['others, no emotion'], 'joy': ['triumphant, gratitude'], 'anger': ['ire, hostility'],
                    'sadness': ['sadness, dismal'], 'surprise': ['unforeseen, breathtaking'],
                    'disgust': ['intolerable, offensive'], 'fear': ['shudder, horror']},
                3: {'noemo': ['others, no emotion'], 'joy': ['cheer, triumphant, bliss'],
                    'anger': ['discontent, hostility, outrage'], 'sadness': ['dismal, grief, depression'],
                    'surprise': ['shocked, unbelievable, unforeseen'], 'disgust': ['displeasure, ugly, offensive'],
                    'fear': ['suspense, terrifying, horror']},
                4: {'noemo': ['others, no emotion'], 'joy': ['cheer, triumphant, joy, bliss'],
                    'anger': ['indignation, hostility, outrage, provocation'],
                    'sadness': ['sadness, dismal, grief, depression'],
                    'surprise': ['shocked, unbelievable, amazing, unforeseen'],
                    'disgust': ['bitter, ugly, offensive, nausea'], 'fear': ['fright, suspense, terrifying, horror']},
                5: {'noemo': ['others, no emotion'], 'joy': ['pleasure, cheer, triumphant, achievement, gratitude'],
                    'anger': ['indignation, hostility, anger, aversion, provocation'],
                    'sadness': ['sadness, grief, tragic, blues, depression'],
                    'surprise': ['shocked, shock, awe, unbelievable, amazing'],
                    'disgust': ['aversion, bitter, ugly, hateful, nausea'],
                    'fear': ['fright, panic, insecurity, horror, chilling']}, 6: {'noemo': ['others, no emotion'], 'joy': [
                    'pleasure, cheer, triumphant, gratitude, enchantment, blessed'], 'anger': [
                    'indignation, hostility, fury, outrage, aversion, provocation'], 'sadness': [
                    'sadness, sadly, melancholy, dismal, grief, pathetic'], 'surprise': [
                    'shocked, shock, awe, unbelievable, amazing, sudden'], 'disgust': [
                    'dislike, aversion, contempt, ugly, hateful, nausea'], 'fear': [
                    'fright, worry, panic, insecurity, terrifying, horror']}, 7: {'noemo': ['others, no emotion'], 'joy': [
                    'pleasure, cheer, triumphant, achievement, gratitude, enchantment, blessed'], 'anger': [
                    'ire, indignation, hostility, annoyance, aversion, provocation, hatred'], 'sadness': [
                    'sadness, sadly, melancholy, dismal, grief, pathetic, blues'], 'surprise': [
                    'shocked, startling, shock, awe, amazing, sudden, abrupt'], 'disgust': [
                    'dislike, aversion, contempt, ugly, hateful, vomiting, nausea'], 'fear': [
                    'fright, worry, panic, anxiety, insecurity, terrifying, horror']}, 8: {'noemo': ['others, no emotion'],
                                                                                           'joy': [
                                                                                               'pleasure, cheer, triumphant, achievement, bliss, enchantment, ecstasy, blessed'],
                                                                                           'anger': [
                                                                                               'ire, indignation, hostility, annoyance, enraged, aversion, provocation, hatred'],
                                                                                           'sadness': [
                                                                                               'sadness, sadly, melancholy, dismal, grief, pathetic, blues, depression'],
                                                                                           'surprise': [
                                                                                               'shocked, astonishing, shock, curious, awe, amazing, sudden, abrupt'],
                                                                                           'disgust': [
                                                                                               'dislike, aversion, contempt, ugly, hateful, intolerable, offensive, nausea'],
                                                                                           'fear': [
                                                                                               'scare, fright, worry, panic, anxiety, insecurity, terrifying, horror']},
                9: {'noemo': ['others, no emotion'],
                    'joy': ['pleasure, cheer, triumphant, joy, achievement, bliss, enchantment, ecstasy, blessed'],
                    'anger': ['indignation, hostility, fury, animosity, outrage, provocation, resentment, hatred, malice'],
                    'sadness': ['sadness, sadly, melancholy, dismal, grief, despair, pathetic, blues, depression'],
                    'surprise': ['astonishing, shock, curious, awe, unexpected, amazing, sudden, abrupt, breathtaking'],
                    'disgust': ['dislike, disdain, aversion, contempt, ugly, hateful, disgusting, offensive, vomiting'],
                    'fear': ['apprehension, scare, fright, worry, panic, anxiety, insecurity, terrifying, horror']},
                10: {'noemo': ['others, no emotion'], 'joy': [
                    'pleasure, awesome, cheer, triumphant, joy, achievement, bliss, enchantment, ecstasy, blessed'],
                     'anger': [
                         'ire, indignation, hostility, annoyance, enraged, animosity, rage, provocation, hatred, malice'],
                     'sadness': ['sadness, sadly, melancholy, dismal, grief, despair, tragic, pathetic, blues, depression'],
                     'surprise': [
                         'perplex, shock, curious, awe, unbelievable, unexpected, amazing, sudden, unforeseen, breathtaking'],
                     'disgust': [
                         'dislike, disdain, aversion, contempt, ugly, hateful, disgusting, intolerable, offensive, nausea'],
                     'fear': [
                         'apprehension, scare, fright, agitation, shudder, panic, anxiety, insecurity, terrifying, horror']},
                11: {'noemo': ['others, no emotion'], 'joy': [
                    'delight, pleasure, awesome, cheer, triumphant, joy, achievement, bliss, enchantment, ecstasy, blessed'],
                     'anger': [
                         'indignation, hostility, annoyance, enraged, anger, animosity, outrage, rage, provocation, hatred, malice'],
                     'sadness': [
                         'sadness, sadly, melancholy, dismal, grief, despair, tragic, pathetic, blues, desperate, depression'],
                     'surprise': [
                         'perplex, startling, shock, amazingly, curious, awe, unexpected, amazing, sudden, dramatic, breathtaking'],
                     'disgust': [
                         'dislike, disdain, disgust, aversion, contempt, ugly, hateful, disgusting, intolerable, offensive, nausea'],
                     'fear': [
                         'apprehension, scare, fright, alarm, agitation, shudder, panic, anxiety, insecurity, terrifying, horror']}}
            hypothesis_emo_synspace_LTOS = {
                2: {'noemo': ['others no emotion'], 'joy': ['triumphant gratitude'], 'anger': ['ire hostility'],
                    'sadness': ['sadness dismal'], 'surprise': ['unforeseen breathtaking'],
                    'disgust': ['intolerable offensive'], 'fear': ['shudder horror']},
                3: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant bliss'],
                    'anger': ['discontent hostility outrage'], 'sadness': ['dismal grief depression'],
                    'surprise': ['shocked unbelievable unforeseen'], 'disgust': ['displeasure ugly offensive'],
                    'fear': ['suspense terrifying horror']},
                4: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant joy bliss'],
                    'anger': ['indignation hostility outrage provocation'], 'sadness': ['sadness dismal grief depression'],
                    'surprise': ['shocked unbelievable amazing unforeseen'], 'disgust': ['bitter ugly offensive nausea'],
                    'fear': ['fright suspense terrifying horror']},
                5: {'noemo': ['others no emotion'], 'joy': ['pleasure cheer triumphant achievement gratitude'],
                    'anger': ['indignation hostility anger aversion provocation'],
                    'sadness': ['sadness grief tragic blues depression'],
                    'surprise': ['shocked shock awe unbelievable amazing'],
                    'disgust': ['aversion bitter ugly hateful nausea'],
                    'fear': ['fright panic insecurity horror chilling']},
                6: {'noemo': ['others no emotion'], 'joy': ['pleasure cheer triumphant gratitude enchantment blessed'],
                    'anger': ['indignation hostility fury outrage aversion provocation'],
                    'sadness': ['sadness sadly melancholy dismal grief pathetic'],
                    'surprise': ['shocked shock awe unbelievable amazing sudden'],
                    'disgust': ['dislike aversion contempt ugly hateful nausea'],
                    'fear': ['fright worry panic insecurity terrifying horror']}, 7: {'noemo': ['others no emotion'],
                                                                                      'joy': [
                                                                                          'pleasure cheer triumphant achievement gratitude enchantment blessed'],
                                                                                      'anger': [
                                                                                          'ire indignation hostility annoyance aversion provocation hatred'],
                                                                                      'sadness': [
                                                                                          'sadness sadly melancholy dismal grief pathetic blues'],
                                                                                      'surprise': [
                                                                                          'shocked startling shock awe amazing sudden abrupt'],
                                                                                      'disgust': [
                                                                                          'dislike aversion contempt ugly hateful vomiting nausea'],
                                                                                      'fear': [
                                                                                          'fright worry panic anxiety insecurity terrifying horror']},
                8: {'noemo': ['others no emotion'],
                    'joy': ['pleasure cheer triumphant achievement bliss enchantment ecstasy blessed'],
                    'anger': ['ire indignation hostility annoyance enraged aversion provocation hatred'],
                    'sadness': ['sadness sadly melancholy dismal grief pathetic blues depression'],
                    'surprise': ['shocked astonishing shock curious awe amazing sudden abrupt'],
                    'disgust': ['dislike aversion contempt ugly hateful intolerable offensive nausea'],
                    'fear': ['scare fright worry panic anxiety insecurity terrifying horror']},
                9: {'noemo': ['others no emotion'],
                    'joy': ['pleasure cheer triumphant joy achievement bliss enchantment ecstasy blessed'],
                    'anger': ['indignation hostility fury animosity outrage provocation resentment hatred malice'],
                    'sadness': ['sadness sadly melancholy dismal grief despair pathetic blues depression'],
                    'surprise': ['astonishing shock curious awe unexpected amazing sudden abrupt breathtaking'],
                    'disgust': ['dislike disdain aversion contempt ugly hateful disgusting offensive vomiting'],
                    'fear': ['apprehension scare fright worry panic anxiety insecurity terrifying horror']},
                10: {'noemo': ['others no emotion'],
                     'joy': ['pleasure awesome cheer triumphant joy achievement bliss enchantment ecstasy blessed'],
                     'anger': ['ire indignation hostility annoyance enraged animosity rage provocation hatred malice'],
                     'sadness': ['sadness sadly melancholy dismal grief despair tragic pathetic blues depression'],
                     'surprise': [
                         'perplex shock curious awe unbelievable unexpected amazing sudden unforeseen breathtaking'],
                     'disgust': ['dislike disdain aversion contempt ugly hateful disgusting intolerable offensive nausea'],
                     'fear': ['apprehension scare fright agitation shudder panic anxiety insecurity terrifying horror']},
                11: {'noemo': ['others no emotion'],
                     'joy': ['delight pleasure awesome cheer triumphant joy achievement bliss enchantment ecstasy blessed'],
                     'anger': [
                         'indignation hostility annoyance enraged anger animosity outrage rage provocation hatred malice'],
                     'sadness': [
                         'sadness sadly melancholy dismal grief despair tragic pathetic blues desperate depression'],
                     'surprise': [
                         'perplex startling shock amazingly curious awe unexpected amazing sudden dramatic breathtaking'],
                     'disgust': [
                         'dislike disdain disgust aversion contempt ugly hateful disgusting intolerable offensive nausea'],
                     'fear': [
                         'apprehension scare fright alarm agitation shudder panic anxiety insecurity terrifying horror']}}
            hypothesis_emo_synslash_LTOS = {
                2: {'noemo': ['others/ no emotion'], 'joy': ['triumphant/ gratitude'], 'anger': ['ire/ hostility'],
                    'sadness': ['sadness/ dismal'], 'surprise': ['unforeseen/ breathtaking'],
                    'disgust': ['intolerable/ offensive'], 'fear': ['shudder/ horror']},
                3: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ triumphant/ bliss'],
                    'anger': ['discontent/ hostility/ outrage'], 'sadness': ['dismal/ grief/ depression'],
                    'surprise': ['shocked/ unbelievable/ unforeseen'], 'disgust': ['displeasure/ ugly/ offensive'],
                    'fear': ['suspense/ terrifying/ horror']},
                4: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ triumphant/ joy/ bliss'],
                    'anger': ['indignation/ hostility/ outrage/ provocation'],
                    'sadness': ['sadness/ dismal/ grief/ depression'],
                    'surprise': ['shocked/ unbelievable/ amazing/ unforeseen'],
                    'disgust': ['bitter/ ugly/ offensive/ nausea'], 'fear': ['fright/ suspense/ terrifying/ horror']},
                5: {'noemo': ['others/ no emotion'], 'joy': ['pleasure/ cheer/ triumphant/ achievement/ gratitude'],
                    'anger': ['indignation/ hostility/ anger/ aversion/ provocation'],
                    'sadness': ['sadness/ grief/ tragic/ blues/ depression'],
                    'surprise': ['shocked/ shock/ awe/ unbelievable/ amazing'],
                    'disgust': ['aversion/ bitter/ ugly/ hateful/ nausea'],
                    'fear': ['fright/ panic/ insecurity/ horror/ chilling']}, 6: {'noemo': ['others/ no emotion'], 'joy': [
                    'pleasure/ cheer/ triumphant/ gratitude/ enchantment/ blessed'], 'anger': [
                    'indignation/ hostility/ fury/ outrage/ aversion/ provocation'], 'sadness': [
                    'sadness/ sadly/ melancholy/ dismal/ grief/ pathetic'], 'surprise': [
                    'shocked/ shock/ awe/ unbelievable/ amazing/ sudden'], 'disgust': [
                    'dislike/ aversion/ contempt/ ugly/ hateful/ nausea'], 'fear': [
                    'fright/ worry/ panic/ insecurity/ terrifying/ horror']}, 7: {'noemo': ['others/ no emotion'], 'joy': [
                    'pleasure/ cheer/ triumphant/ achievement/ gratitude/ enchantment/ blessed'], 'anger': [
                    'ire/ indignation/ hostility/ annoyance/ aversion/ provocation/ hatred'], 'sadness': [
                    'sadness/ sadly/ melancholy/ dismal/ grief/ pathetic/ blues'], 'surprise': [
                    'shocked/ startling/ shock/ awe/ amazing/ sudden/ abrupt'], 'disgust': [
                    'dislike/ aversion/ contempt/ ugly/ hateful/ vomiting/ nausea'], 'fear': [
                    'fright/ worry/ panic/ anxiety/ insecurity/ terrifying/ horror']}, 8: {'noemo': ['others/ no emotion'],
                                                                                           'joy': [
                                                                                               'pleasure/ cheer/ triumphant/ achievement/ bliss/ enchantment/ ecstasy/ blessed'],
                                                                                           'anger': [
                                                                                               'ire/ indignation/ hostility/ annoyance/ enraged/ aversion/ provocation/ hatred'],
                                                                                           'sadness': [
                                                                                               'sadness/ sadly/ melancholy/ dismal/ grief/ pathetic/ blues/ depression'],
                                                                                           'surprise': [
                                                                                               'shocked/ astonishing/ shock/ curious/ awe/ amazing/ sudden/ abrupt'],
                                                                                           'disgust': [
                                                                                               'dislike/ aversion/ contempt/ ugly/ hateful/ intolerable/ offensive/ nausea'],
                                                                                           'fear': [
                                                                                               'scare/ fright/ worry/ panic/ anxiety/ insecurity/ terrifying/ horror']},
                9: {'noemo': ['others/ no emotion'],
                    'joy': ['pleasure/ cheer/ triumphant/ joy/ achievement/ bliss/ enchantment/ ecstasy/ blessed'],
                    'anger': ['indignation/ hostility/ fury/ animosity/ outrage/ provocation/ resentment/ hatred/ malice'],
                    'sadness': ['sadness/ sadly/ melancholy/ dismal/ grief/ despair/ pathetic/ blues/ depression'],
                    'surprise': ['astonishing/ shock/ curious/ awe/ unexpected/ amazing/ sudden/ abrupt/ breathtaking'],
                    'disgust': ['dislike/ disdain/ aversion/ contempt/ ugly/ hateful/ disgusting/ offensive/ vomiting'],
                    'fear': ['apprehension/ scare/ fright/ worry/ panic/ anxiety/ insecurity/ terrifying/ horror']},
                10: {'noemo': ['others/ no emotion'], 'joy': [
                    'pleasure/ awesome/ cheer/ triumphant/ joy/ achievement/ bliss/ enchantment/ ecstasy/ blessed'],
                     'anger': [
                         'ire/ indignation/ hostility/ annoyance/ enraged/ animosity/ rage/ provocation/ hatred/ malice'],
                     'sadness': ['sadness/ sadly/ melancholy/ dismal/ grief/ despair/ tragic/ pathetic/ blues/ depression'],
                     'surprise': [
                         'perplex/ shock/ curious/ awe/ unbelievable/ unexpected/ amazing/ sudden/ unforeseen/ breathtaking'],
                     'disgust': [
                         'dislike/ disdain/ aversion/ contempt/ ugly/ hateful/ disgusting/ intolerable/ offensive/ nausea'],
                     'fear': [
                         'apprehension/ scare/ fright/ agitation/ shudder/ panic/ anxiety/ insecurity/ terrifying/ horror']},
                11: {'noemo': ['others/ no emotion'], 'joy': [
                    'delight/ pleasure/ awesome/ cheer/ triumphant/ joy/ achievement/ bliss/ enchantment/ ecstasy/ blessed'],
                     'anger': [
                         'indignation/ hostility/ annoyance/ enraged/ anger/ animosity/ outrage/ rage/ provocation/ hatred/ malice'],
                     'sadness': [
                         'sadness/ sadly/ melancholy/ dismal/ grief/ despair/ tragic/ pathetic/ blues/ desperate/ depression'],
                     'surprise': [
                         'perplex/ startling/ shock/ amazingly/ curious/ awe/ unexpected/ amazing/ sudden/ dramatic/ breathtaking'],
                     'disgust': [
                         'dislike/ disdain/ disgust/ aversion/ contempt/ ugly/ hateful/ disgusting/ intolerable/ offensive/ nausea'],
                     'fear': [
                         'apprehension/ scare/ fright/ alarm/ agitation/ shudder/ panic/ anxiety/ insecurity/ terrifying/ horror']}}
            hypothesis_emo_synsand_LTOS = {
                2: {'noemo': ['others and no emotion'], 'joy': ['triumphant and gratitude'], 'anger': ['ire and hostility'],
                    'sadness': ['sadness and dismal'], 'surprise': ['unforeseen and breathtaking'],
                    'disgust': ['intolerable and offensive'], 'fear': ['shudder and horror']},
                3: {'noemo': ['others and no emotion'], 'joy': ['cheer and triumphant and bliss'],
                    'anger': ['discontent and hostility and outrage'], 'sadness': ['dismal and grief and depression'],
                    'surprise': ['shocked and unbelievable and unforeseen'],
                    'disgust': ['displeasure and ugly and offensive'], 'fear': ['suspense and terrifying and horror']},
                4: {'noemo': ['others and no emotion'], 'joy': ['cheer and triumphant and joy and bliss'],
                    'anger': ['indignation and hostility and outrage and provocation'],
                    'sadness': ['sadness and dismal and grief and depression'],
                    'surprise': ['shocked and unbelievable and amazing and unforeseen'],
                    'disgust': ['bitter and ugly and offensive and nausea'],
                    'fear': ['fright and suspense and terrifying and horror']}, 5: {'noemo': ['others and no emotion'],
                                                                                    'joy': [
                                                                                        'pleasure and cheer and triumphant and achievement and gratitude'],
                                                                                    'anger': [
                                                                                        'indignation and hostility and anger and aversion and provocation'],
                                                                                    'sadness': [
                                                                                        'sadness and grief and tragic and blues and depression'],
                                                                                    'surprise': [
                                                                                        'shocked and shock and awe and unbelievable and amazing'],
                                                                                    'disgust': [
                                                                                        'aversion and bitter and ugly and hateful and nausea'],
                                                                                    'fear': [
                                                                                        'fright and panic and insecurity and horror and chilling']},
                6: {'noemo': ['others and no emotion'],
                    'joy': ['pleasure and cheer and triumphant and gratitude and enchantment and blessed'],
                    'anger': ['indignation and hostility and fury and outrage and aversion and provocation'],
                    'sadness': ['sadness and sadly and melancholy and dismal and grief and pathetic'],
                    'surprise': ['shocked and shock and awe and unbelievable and amazing and sudden'],
                    'disgust': ['dislike and aversion and contempt and ugly and hateful and nausea'],
                    'fear': ['fright and worry and panic and insecurity and terrifying and horror']},
                7: {'noemo': ['others and no emotion'],
                    'joy': ['pleasure and cheer and triumphant and achievement and gratitude and enchantment and blessed'],
                    'anger': ['ire and indignation and hostility and annoyance and aversion and provocation and hatred'],
                    'sadness': ['sadness and sadly and melancholy and dismal and grief and pathetic and blues'],
                    'surprise': ['shocked and startling and shock and awe and amazing and sudden and abrupt'],
                    'disgust': ['dislike and aversion and contempt and ugly and hateful and vomiting and nausea'],
                    'fear': ['fright and worry and panic and anxiety and insecurity and terrifying and horror']},
                8: {'noemo': ['others and no emotion'], 'joy': [
                    'pleasure and cheer and triumphant and achievement and bliss and enchantment and ecstasy and blessed'],
                    'anger': [
                        'ire and indignation and hostility and annoyance and enraged and aversion and provocation and hatred'],
                    'sadness': [
                        'sadness and sadly and melancholy and dismal and grief and pathetic and blues and depression'],
                    'surprise': ['shocked and astonishing and shock and curious and awe and amazing and sudden and abrupt'],
                    'disgust': [
                        'dislike and aversion and contempt and ugly and hateful and intolerable and offensive and nausea'],
                    'fear': ['scare and fright and worry and panic and anxiety and insecurity and terrifying and horror']},
                9: {'noemo': ['others and no emotion'], 'joy': [
                    'pleasure and cheer and triumphant and joy and achievement and bliss and enchantment and ecstasy and blessed'],
                    'anger': [
                        'indignation and hostility and fury and animosity and outrage and provocation and resentment and hatred and malice'],
                    'sadness': [
                        'sadness and sadly and melancholy and dismal and grief and despair and pathetic and blues and depression'],
                    'surprise': [
                        'astonishing and shock and curious and awe and unexpected and amazing and sudden and abrupt and breathtaking'],
                    'disgust': [
                        'dislike and disdain and aversion and contempt and ugly and hateful and disgusting and offensive and vomiting'],
                    'fear': [
                        'apprehension and scare and fright and worry and panic and anxiety and insecurity and terrifying and horror']},
                10: {'noemo': ['others and no emotion'], 'joy': [
                    'pleasure and awesome and cheer and triumphant and joy and achievement and bliss and enchantment and ecstasy and blessed'],
                     'anger': [
                         'ire and indignation and hostility and annoyance and enraged and animosity and rage and provocation and hatred and malice'],
                     'sadness': [
                         'sadness and sadly and melancholy and dismal and grief and despair and tragic and pathetic and blues and depression'],
                     'surprise': [
                         'perplex and shock and curious and awe and unbelievable and unexpected and amazing and sudden and unforeseen and breathtaking'],
                     'disgust': [
                         'dislike and disdain and aversion and contempt and ugly and hateful and disgusting and intolerable and offensive and nausea'],
                     'fear': [
                         'apprehension and scare and fright and agitation and shudder and panic and anxiety and insecurity and terrifying and horror']},
                11: {'noemo': ['others and no emotion'], 'joy': [
                    'delight and pleasure and awesome and cheer and triumphant and joy and achievement and bliss and enchantment and ecstasy and blessed'],
                     'anger': [
                         'indignation and hostility and annoyance and enraged and anger and animosity and outrage and rage and provocation and hatred and malice'],
                     'sadness': [
                         'sadness and sadly and melancholy and dismal and grief and despair and tragic and pathetic and blues and desperate and depression'],
                     'surprise': [
                         'perplex and startling and shock and amazingly and curious and awe and unexpected and amazing and sudden and dramatic and breathtaking'],
                     'disgust': [
                         'dislike and disdain and disgust and aversion and contempt and ugly and hateful and disgusting and intolerable and offensive and nausea'],
                     'fear': [
                         'apprehension and scare and fright and alarm and agitation and shudder and panic and anxiety and insecurity and terrifying and horror']}}
        hypothesis = f'./hypothesis_final/hypothesis_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num} \n')
                    if td == 'test':
                        for n in range(5):
                            savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str( num) +  '_' + sprompt+'_' + td +'entail_'+str(n)+'.csv'
                            modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str( num) +  '_' + sprompt+'_' + td +'_'+str(n)+'.csv'
                            train = './data/' + dataname.upper() + '/' + dataname.lower() +'select_'+td+'02_'+str(n)+'.csv'
                            rows = []

                            with open(train) as f:
                                csv_read = csv.reader(f)

                                for row in csv_read:
                                    label = ['joy', 'anger', 'sadness', 'surprise', 'disgust', 'noemo',
                                             'fear']
                                    for l in label:
                                        with open(hypothesis) as tf:
                                            csv_temp = csv.reader(tf)
                                            for tem in csv_temp:
                                                if sprompt=='syns':
                                                    hypothesis_emo_s = hypothesis_emo_syns_LTOS[num]
                                                elif sprompt=='synspace':
                                                    hypothesis_emo_s = hypothesis_emo_synspace_LTOS[num]
                                                elif sprompt == 'synslash':
                                                    hypothesis_emo_s = hypothesis_emo_synslash_LTOS[num]
                                                elif sprompt == 'synsand':
                                                    hypothesis_emo_s = hypothesis_emo_synsand_LTOS[num]
                                                else:
                                                    print('error')
                                                    exit()
                                                st = []
                                                st.append(row[0])
                                                truetem = tem[0].replace('M', hypothesis_emo_s[l][0])
                                                st.append(truetem)
                                                if l == row[1]:
                                                    st.append('entailment')
                                                else:
                                                    st.append('contradiction')
                                                st.append(row[1])
                                                st.append(l)
                                                rows.append(st)

                            with open(modifiedfile, 'w', newline='') as f:
                                f_csv = csv.writer(f)
                                f_csv.writerows(rows)
                            combine(modifiedfile,savefile)

                    else:
                        for n in range(5):
                            savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_'+ sprompt+'_' + td + 'entail_' + str(n) + '.csv'
                            modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_'+ sprompt+'_' + td + '_' + str(n) + '.csv'
                            train = './data/' + dataname.upper() + '/' + dataname.lower() + 'select_' + td + '_' + str(
                                n) + '.csv'
                            rows = []
                            with open(train) as f:
                                csv_read = csv.reader(f)

                                for row in csv_read:
                                    with open(hypothesis) as tf:
                                        csv_temp = csv.reader(tf)
                                        for tem in csv_temp:
                                            if sprompt == 'syns':
                                                hypothesis_emo_s = hypothesis_emo_syns_LTOS[num]
                                            elif sprompt == 'synspace':
                                                hypothesis_emo_s = hypothesis_emo_synspace_LTOS[num]
                                            elif sprompt == 'synslash':
                                                hypothesis_emo_s = hypothesis_emo_synslash_LTOS[num]
                                            elif sprompt == 'synsand':
                                                hypothesis_emo_s = hypothesis_emo_synsand_LTOS[num]
                                            else:
                                                print('error')
                                                exit()

                                            label = ['joy', 'anger', 'sadness', 'surprise', 'disgust', 'noemo',
                                                     'fear']  # aman

                                            st=[]
                                            st.append(row[0])
                                            truetem=tem[0].replace('M',hypothesis_emo_s[row[1]][0])
                                            st.append(truetem)
                                            st.append('entailment')
                                            st.append(row[1])
                                            st.append(row[1])
                                            rows.append(st)
                                            label.remove(row[1])
                                            falselabelselect = sample(label, 1)
                                            for falselabel in falselabelselect:
                                                st = []
                                                st.append(row[0])
                                                falsetem = tem[0].replace("M", hypothesis_emo_s[falselabel][0])
                                                st.append(falsetem)
                                                st.append('contradiction')
                                                st.append(row[1])
                                                st.append(falselabel)
                                                rows.append(st)



                            with open(modifiedfile, 'w', newline='') as f:
                                f_csv = csv.writer(f)
                                f_csv.writerows(rows)
                            combine(modifiedfile, savefile)

def mainmeld(k):
    datasetnames = [
        'meld'
    ]
    traindev = [
        'train', 'dev',
        'test']
    if k == 'freq':
        hypothesis_emo_syns_LTOS = {
            2: {'noemo': ['others, no emotion'], 'joy': ['gratitude, triumphant'], 'anger': ['hostility, ire'],
                'sadness': ['sadness, dismal'], 'surprise': ['unforeseen, breathtaking'],
                'disgust': ['offensive, intolerable'], 'fear': ['horror, shudder']},
            3: {'noemo': ['others, no emotion'], 'joy': ['cheer, bliss, triumphant'],
                'anger': ['hostility, outrage, discontent'], 'sadness': ['depression, grief, dismal'],
                'surprise': ['shocked, unbelievable, unforeseen'], 'disgust': ['ugly, offensive, displeasure'],
                'fear': ['horror, terrifying, suspense']},
            4: {'noemo': ['others, no emotion'], 'joy': ['joy, cheer, bliss, triumphant'],
                'anger': ['hostility, indignation, outrage, provocation'],
                'sadness': ['depression, grief, sadness, dismal'],
                'surprise': ['amazing, shocked, unbelievable, unforeseen'],
                'disgust': ['bitter, ugly, offensive, nausea'], 'fear': ['horror, terrifying, fright, suspense']},
            5: {'noemo': ['others, no emotion'], 'joy': ['pleasure, achievement, gratitude, cheer, triumphant'],
                'anger': ['anger, hostility, indignation, aversion, provocation'],
                'sadness': ['depression, grief, sadness, tragic, blues'],
                'surprise': ['shock, amazing, shocked, awe, unbelievable'],
                'disgust': ['bitter, ugly, nausea, aversion, hateful'],
                'fear': ['horror, panic, insecurity, fright, chilling']}, 6: {'noemo': ['others, no emotion'],
                                                                              'joy': [
                                                                                  'pleasure, blessed, gratitude, cheer, triumphant, enchantment'],
                                                                              'anger': [
                                                                                  'fury, hostility, indignation, outrage, aversion, provocation'],
                                                                              'sadness': [
                                                                                  'grief, sadness, melancholy, sadly, pathetic, dismal'],
                                                                              'surprise': [
                                                                                  'sudden, shock, amazing, shocked, awe, unbelievable'],
                                                                              'disgust': [
                                                                                  'ugly, contempt, dislike, nausea, aversion, hateful'],
                                                                              'fear': [
                                                                                  'worry, horror, panic, terrifying, insecurity, fright']},
            7: {'noemo': ['others, no emotion'],
                'joy': ['pleasure, achievement, blessed, gratitude, cheer, triumphant, enchantment'],
                'anger': ['hatred, hostility, indignation, annoyance, aversion, provocation, ire'],
                'sadness': ['grief, sadness, melancholy, sadly, pathetic, blues, dismal'],
                'surprise': ['sudden, shock, amazing, shocked, awe, abrupt, startling'],
                'disgust': ['ugly, contempt, dislike, nausea, vomiting, aversion, hateful'],
                'fear': ['worry, anxiety, horror, panic, terrifying, insecurity, fright']},
            8: {'noemo': ['others, no emotion'],
                'joy': ['pleasure, achievement, blessed, cheer, bliss, ecstasy, triumphant, enchantment'],
                'anger': ['hatred, hostility, indignation, annoyance, aversion, enraged, provocation, ire'],
                'sadness': ['depression, grief, sadness, melancholy, sadly, pathetic, blues, dismal'],
                'surprise': ['sudden, shock, curious, amazing, shocked, awe, abrupt, astonishing'],
                'disgust': ['ugly, offensive, contempt, dislike, nausea, aversion, intolerable, hateful'],
                'fear': ['worry, anxiety, horror, panic, terrifying, scare, insecurity, fright']},
            9: {'noemo': ['others, no emotion'],
                'joy': ['pleasure, joy, achievement, blessed, cheer, bliss, ecstasy, triumphant, enchantment'],
                'anger': [
                    'hatred, fury, resentment, hostility, indignation, outrage, malice, provocation, animosity'],
                'sadness': ['depression, grief, despair, sadness, melancholy, sadly, pathetic, blues, dismal'],
                'surprise': ['sudden, shock, curious, amazing, unexpected, awe, abrupt, astonishing, breathtaking'],
                'disgust': ['ugly, offensive, contempt, dislike, vomiting, disdain, aversion, disgusting, hateful'],
                'fear': ['worry, anxiety, horror, panic, terrifying, apprehension, scare, insecurity, fright']},
            10: {'noemo': ['others, no emotion'], 'joy': [
                'pleasure, joy, achievement, blessed, cheer, awesome, bliss, ecstasy, triumphant, enchantment'],
                 'anger': [
                     'rage, hatred, hostility, indignation, annoyance, malice, enraged, provocation, animosity, ire'],
                 'sadness': [
                     'depression, grief, despair, sadness, tragic, melancholy, sadly, pathetic, blues, dismal'],
                 'surprise': [
                     'sudden, shock, curious, amazing, unexpected, awe, unbelievable, unforeseen, breathtaking, perplex'],
                 'disgust': [
                     'ugly, offensive, contempt, dislike, nausea, disdain, aversion, disgusting, intolerable, hateful'],
                 'fear': [
                     'anxiety, horror, panic, terrifying, agitation, apprehension, scare, insecurity, shudder, fright']},
            11: {'noemo': ['others, no emotion'], 'joy': [
                'pleasure, joy, delight, achievement, blessed, cheer, awesome, bliss, ecstasy, triumphant, enchantment'],
                 'anger': [
                     'anger, rage, hatred, hostility, indignation, annoyance, outrage, malice, enraged, provocation, animosity'],
                 'sadness': [
                     'depression, grief, desperate, despair, sadness, tragic, melancholy, sadly, pathetic, blues, dismal'],
                 'surprise': [
                     'sudden, shock, curious, amazing, dramatic, unexpected, awe, startling, amazingly, breathtaking, perplex'],
                 'disgust': [
                     'ugly, offensive, contempt, disgust, dislike, nausea, disdain, aversion, disgusting, intolerable, hateful'],
                 'fear': [
                     'anxiety, horror, panic, alarm, terrifying, agitation, apprehension, scare, insecurity, shudder, fright']}}
        hypothesis_emo_synspace_LTOS = {
            2: {'noemo': ['others no emotion'], 'joy': ['gratitude triumphant'], 'anger': ['hostility ire'],
                'sadness': ['sadness dismal'], 'surprise': ['unforeseen breathtaking'],
                'disgust': ['offensive intolerable'], 'fear': ['horror shudder']},
            3: {'noemo': ['others no emotion'], 'joy': ['cheer bliss triumphant'],
                'anger': ['hostility outrage discontent'], 'sadness': ['depression grief dismal'],
                'surprise': ['shocked unbelievable unforeseen'], 'disgust': ['ugly offensive displeasure'],
                'fear': ['horror terrifying suspense']},
            4: {'noemo': ['others no emotion'], 'joy': ['joy cheer bliss triumphant'],
                'anger': ['hostility indignation outrage provocation'],
                'sadness': ['depression grief sadness dismal'],
                'surprise': ['amazing shocked unbelievable unforeseen'],
                'disgust': ['bitter ugly offensive nausea'], 'fear': ['horror terrifying fright suspense']},
            5: {'noemo': ['others no emotion'], 'joy': ['pleasure achievement gratitude cheer triumphant'],
                'anger': ['anger hostility indignation aversion provocation'],
                'sadness': ['depression grief sadness tragic blues'],
                'surprise': ['shock amazing shocked awe unbelievable'],
                'disgust': ['bitter ugly nausea aversion hateful'],
                'fear': ['horror panic insecurity fright chilling']},
            6: {'noemo': ['others no emotion'], 'joy': ['pleasure blessed gratitude cheer triumphant enchantment'],
                'anger': ['fury hostility indignation outrage aversion provocation'],
                'sadness': ['grief sadness melancholy sadly pathetic dismal'],
                'surprise': ['sudden shock amazing shocked awe unbelievable'],
                'disgust': ['ugly contempt dislike nausea aversion hateful'],
                'fear': ['worry horror panic terrifying insecurity fright']}, 7: {'noemo': ['others no emotion'],
                                                                                  'joy': [
                                                                                      'pleasure achievement blessed gratitude cheer triumphant enchantment'],
                                                                                  'anger': [
                                                                                      'hatred hostility indignation annoyance aversion provocation ire'],
                                                                                  'sadness': [
                                                                                      'grief sadness melancholy sadly pathetic blues dismal'],
                                                                                  'surprise': [
                                                                                      'sudden shock amazing shocked awe abrupt startling'],
                                                                                  'disgust': [
                                                                                      'ugly contempt dislike nausea vomiting aversion hateful'],
                                                                                  'fear': [
                                                                                      'worry anxiety horror panic terrifying insecurity fright']},
            8: {'noemo': ['others no emotion'],
                'joy': ['pleasure achievement blessed cheer bliss ecstasy triumphant enchantment'],
                'anger': ['hatred hostility indignation annoyance aversion enraged provocation ire'],
                'sadness': ['depression grief sadness melancholy sadly pathetic blues dismal'],
                'surprise': ['sudden shock curious amazing shocked awe abrupt astonishing'],
                'disgust': ['ugly offensive contempt dislike nausea aversion intolerable hateful'],
                'fear': ['worry anxiety horror panic terrifying scare insecurity fright']},
            9: {'noemo': ['others no emotion'],
                'joy': ['pleasure joy achievement blessed cheer bliss ecstasy triumphant enchantment'],
                'anger': ['hatred fury resentment hostility indignation outrage malice provocation animosity'],
                'sadness': ['depression grief despair sadness melancholy sadly pathetic blues dismal'],
                'surprise': ['sudden shock curious amazing unexpected awe abrupt astonishing breathtaking'],
                'disgust': ['ugly offensive contempt dislike vomiting disdain aversion disgusting hateful'],
                'fear': ['worry anxiety horror panic terrifying apprehension scare insecurity fright']},
            10: {'noemo': ['others no emotion'],
                 'joy': ['pleasure joy achievement blessed cheer awesome bliss ecstasy triumphant enchantment'],
                 'anger': ['rage hatred hostility indignation annoyance malice enraged provocation animosity ire'],
                 'sadness': ['depression grief despair sadness tragic melancholy sadly pathetic blues dismal'],
                 'surprise': [
                     'sudden shock curious amazing unexpected awe unbelievable unforeseen breathtaking perplex'],
                 'disgust': [
                     'ugly offensive contempt dislike nausea disdain aversion disgusting intolerable hateful'],
                 'fear': [
                     'anxiety horror panic terrifying agitation apprehension scare insecurity shudder fright']},
            11: {'noemo': ['others no emotion'], 'joy': [
                'pleasure joy delight achievement blessed cheer awesome bliss ecstasy triumphant enchantment'],
                 'anger': [
                     'anger rage hatred hostility indignation annoyance outrage malice enraged provocation animosity'],
                 'sadness': [
                     'depression grief desperate despair sadness tragic melancholy sadly pathetic blues dismal'],
                 'surprise': [
                     'sudden shock curious amazing dramatic unexpected awe startling amazingly breathtaking perplex'],
                 'disgust': [
                     'ugly offensive contempt disgust dislike nausea disdain aversion disgusting intolerable hateful'],
                 'fear': [
                     'anxiety horror panic alarm terrifying agitation apprehension scare insecurity shudder fright']}}
        hypothesis_emo_synslash_LTOS = {
            2: {'noemo': ['others/ no emotion'], 'joy': ['gratitude/ triumphant'], 'anger': ['hostility/ ire'],
                'sadness': ['sadness/ dismal'], 'surprise': ['unforeseen/ breathtaking'],
                'disgust': ['offensive/ intolerable'], 'fear': ['horror/ shudder']},
            3: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ bliss/ triumphant'],
                'anger': ['hostility/ outrage/ discontent'], 'sadness': ['depression/ grief/ dismal'],
                'surprise': ['shocked/ unbelievable/ unforeseen'], 'disgust': ['ugly/ offensive/ displeasure'],
                'fear': ['horror/ terrifying/ suspense']},
            4: {'noemo': ['others/ no emotion'], 'joy': ['joy/ cheer/ bliss/ triumphant'],
                'anger': ['hostility/ indignation/ outrage/ provocation'],
                'sadness': ['depression/ grief/ sadness/ dismal'],
                'surprise': ['amazing/ shocked/ unbelievable/ unforeseen'],
                'disgust': ['bitter/ ugly/ offensive/ nausea'], 'fear': ['horror/ terrifying/ fright/ suspense']},
            5: {'noemo': ['others/ no emotion'], 'joy': ['pleasure/ achievement/ gratitude/ cheer/ triumphant'],
                'anger': ['anger/ hostility/ indignation/ aversion/ provocation'],
                'sadness': ['depression/ grief/ sadness/ tragic/ blues'],
                'surprise': ['shock/ amazing/ shocked/ awe/ unbelievable'],
                'disgust': ['bitter/ ugly/ nausea/ aversion/ hateful'],
                'fear': ['horror/ panic/ insecurity/ fright/ chilling']}, 6: {'noemo': ['others/ no emotion'],
                                                                              'joy': [
                                                                                  'pleasure/ blessed/ gratitude/ cheer/ triumphant/ enchantment'],
                                                                              'anger': [
                                                                                  'fury/ hostility/ indignation/ outrage/ aversion/ provocation'],
                                                                              'sadness': [
                                                                                  'grief/ sadness/ melancholy/ sadly/ pathetic/ dismal'],
                                                                              'surprise': [
                                                                                  'sudden/ shock/ amazing/ shocked/ awe/ unbelievable'],
                                                                              'disgust': [
                                                                                  'ugly/ contempt/ dislike/ nausea/ aversion/ hateful'],
                                                                              'fear': [
                                                                                  'worry/ horror/ panic/ terrifying/ insecurity/ fright']},
            7: {'noemo': ['others/ no emotion'],
                'joy': ['pleasure/ achievement/ blessed/ gratitude/ cheer/ triumphant/ enchantment'],
                'anger': ['hatred/ hostility/ indignation/ annoyance/ aversion/ provocation/ ire'],
                'sadness': ['grief/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                'surprise': ['sudden/ shock/ amazing/ shocked/ awe/ abrupt/ startling'],
                'disgust': ['ugly/ contempt/ dislike/ nausea/ vomiting/ aversion/ hateful'],
                'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ insecurity/ fright']},
            8: {'noemo': ['others/ no emotion'],
                'joy': ['pleasure/ achievement/ blessed/ cheer/ bliss/ ecstasy/ triumphant/ enchantment'],
                'anger': ['hatred/ hostility/ indignation/ annoyance/ aversion/ enraged/ provocation/ ire'],
                'sadness': ['depression/ grief/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                'surprise': ['sudden/ shock/ curious/ amazing/ shocked/ awe/ abrupt/ astonishing'],
                'disgust': ['ugly/ offensive/ contempt/ dislike/ nausea/ aversion/ intolerable/ hateful'],
                'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ scare/ insecurity/ fright']},
            9: {'noemo': ['others/ no emotion'],
                'joy': ['pleasure/ joy/ achievement/ blessed/ cheer/ bliss/ ecstasy/ triumphant/ enchantment'],
                'anger': [
                    'hatred/ fury/ resentment/ hostility/ indignation/ outrage/ malice/ provocation/ animosity'],
                'sadness': ['depression/ grief/ despair/ sadness/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                'surprise': ['sudden/ shock/ curious/ amazing/ unexpected/ awe/ abrupt/ astonishing/ breathtaking'],
                'disgust': ['ugly/ offensive/ contempt/ dislike/ vomiting/ disdain/ aversion/ disgusting/ hateful'],
                'fear': ['worry/ anxiety/ horror/ panic/ terrifying/ apprehension/ scare/ insecurity/ fright']},
            10: {'noemo': ['others/ no emotion'], 'joy': [
                'pleasure/ joy/ achievement/ blessed/ cheer/ awesome/ bliss/ ecstasy/ triumphant/ enchantment'],
                 'anger': [
                     'rage/ hatred/ hostility/ indignation/ annoyance/ malice/ enraged/ provocation/ animosity/ ire'],
                 'sadness': [
                     'depression/ grief/ despair/ sadness/ tragic/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                 'surprise': [
                     'sudden/ shock/ curious/ amazing/ unexpected/ awe/ unbelievable/ unforeseen/ breathtaking/ perplex'],
                 'disgust': [
                     'ugly/ offensive/ contempt/ dislike/ nausea/ disdain/ aversion/ disgusting/ intolerable/ hateful'],
                 'fear': [
                     'anxiety/ horror/ panic/ terrifying/ agitation/ apprehension/ scare/ insecurity/ shudder/ fright']},
            11: {'noemo': ['others/ no emotion'], 'joy': [
                'pleasure/ joy/ delight/ achievement/ blessed/ cheer/ awesome/ bliss/ ecstasy/ triumphant/ enchantment'],
                 'anger': [
                     'anger/ rage/ hatred/ hostility/ indignation/ annoyance/ outrage/ malice/ enraged/ provocation/ animosity'],
                 'sadness': [
                     'depression/ grief/ desperate/ despair/ sadness/ tragic/ melancholy/ sadly/ pathetic/ blues/ dismal'],
                 'surprise': [
                     'sudden/ shock/ curious/ amazing/ dramatic/ unexpected/ awe/ startling/ amazingly/ breathtaking/ perplex'],
                 'disgust': [
                     'ugly/ offensive/ contempt/ disgust/ dislike/ nausea/ disdain/ aversion/ disgusting/ intolerable/ hateful'],
                 'fear': [
                     'anxiety/ horror/ panic/ alarm/ terrifying/ agitation/ apprehension/ scare/ insecurity/ shudder/ fright']}}
        hypothesis_emo_synsand_LTOS = {
            2: {'noemo': ['others and no emotion'], 'joy': ['gratitude and triumphant'],
                'anger': ['hostility and ire'], 'sadness': ['sadness and dismal'],
                'surprise': ['unforeseen and breathtaking'],
                'disgust': ['offensive and intolerable'], 'fear': ['horror and shudder']},
            3: {'noemo': ['others and no emotion'],
                'joy': ['cheer and bliss and triumphant'],
                'anger': ['hostility and outrage and discontent'],
                'sadness': ['depression and grief and dismal'],
                'surprise': ['shocked and unbelievable and unforeseen'],
                'disgust': ['ugly and offensive and displeasure'],
                'fear': ['horror and terrifying and suspense']},
            4: {'noemo': ['others and no emotion'],
                'joy': ['joy and cheer and bliss and triumphant'],
                'anger': ['hostility and indignation and outrage and provocation'],
                'sadness': ['depression and grief and sadness and dismal'],
                'surprise': ['amazing and shocked and unbelievable and unforeseen'],
                'disgust': ['bitter and ugly and offensive and nausea'],
                'fear': ['horror and terrifying and fright and suspense']},
            5: {'noemo': ['others and no emotion'],
                'joy': ['pleasure and achievement and gratitude and cheer and triumphant'],
                'anger': [
                    'anger and hostility and indignation and aversion and provocation'],
                'sadness': ['depression and grief and sadness and tragic and blues'],
                'surprise': ['shock and amazing and shocked and awe and unbelievable'],
                'disgust': ['bitter and ugly and nausea and aversion and hateful'],
                'fear': ['horror and panic and insecurity and fright and chilling']},
            6: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and blessed and gratitude and cheer and triumphant and enchantment'],
                'anger': [
                    'fury and hostility and indignation and outrage and aversion and provocation'],
                'sadness': [
                    'grief and sadness and melancholy and sadly and pathetic and dismal'],
                'surprise': [
                    'sudden and shock and amazing and shocked and awe and unbelievable'],
                'disgust': [
                    'ugly and contempt and dislike and nausea and aversion and hateful'],
                'fear': [
                    'worry and horror and panic and terrifying and insecurity and fright']},
            7: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and achievement and blessed and gratitude and cheer and triumphant and enchantment'],
                'anger': [
                    'hatred and hostility and indignation and annoyance and aversion and provocation and ire'],
                'sadness': [
                    'grief and sadness and melancholy and sadly and pathetic and blues and dismal'],
                'surprise': [
                    'sudden and shock and amazing and shocked and awe and abrupt and startling'],
                'disgust': [
                    'ugly and contempt and dislike and nausea and vomiting and aversion and hateful'],
                'fear': [
                    'worry and anxiety and horror and panic and terrifying and insecurity and fright']},
            8: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and achievement and blessed and cheer and bliss and ecstasy and triumphant and enchantment'],
                'anger': [
                    'hatred and hostility and indignation and annoyance and aversion and enraged and provocation and ire'],
                'sadness': [
                    'depression and grief and sadness and melancholy and sadly and pathetic and blues and dismal'],
                'surprise': [
                    'sudden and shock and curious and amazing and shocked and awe and abrupt and astonishing'],
                'disgust': [
                    'ugly and offensive and contempt and dislike and nausea and aversion and intolerable and hateful'],
                'fear': [
                    'worry and anxiety and horror and panic and terrifying and scare and insecurity and fright']},
            9: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and joy and achievement and blessed and cheer and bliss and ecstasy and triumphant and enchantment'],
                'anger': [
                    'hatred and fury and resentment and hostility and indignation and outrage and malice and provocation and animosity'],
                'sadness': [
                    'depression and grief and despair and sadness and melancholy and sadly and pathetic and blues and dismal'],
                'surprise': [
                    'sudden and shock and curious and amazing and unexpected and awe and abrupt and astonishing and breathtaking'],
                'disgust': [
                    'ugly and offensive and contempt and dislike and vomiting and disdain and aversion and disgusting and hateful'],
                'fear': [
                    'worry and anxiety and horror and panic and terrifying and apprehension and scare and insecurity and fright']},
            10: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and joy and achievement and blessed and cheer and awesome and bliss and ecstasy and triumphant and enchantment'],
                 'anger': [
                     'rage and hatred and hostility and indignation and annoyance and malice and enraged and provocation and animosity and ire'],
                 'sadness': [
                     'depression and grief and despair and sadness and tragic and melancholy and sadly and pathetic and blues and dismal'],
                 'surprise': [
                     'sudden and shock and curious and amazing and unexpected and awe and unbelievable and unforeseen and breathtaking and perplex'],
                 'disgust': [
                     'ugly and offensive and contempt and dislike and nausea and disdain and aversion and disgusting and intolerable and hateful'],
                 'fear': [
                     'anxiety and horror and panic and terrifying and agitation and apprehension and scare and insecurity and shudder and fright']},
            11: {'noemo': ['others and no emotion'], 'joy': [
                'pleasure and joy and delight and achievement and blessed and cheer and awesome and bliss and ecstasy and triumphant and enchantment'],
                 'anger': [
                     'anger and rage and hatred and hostility and indignation and annoyance and outrage and malice and enraged and provocation and animosity'],
                 'sadness': [
                     'depression and grief and desperate and despair and sadness and tragic and melancholy and sadly and pathetic and blues and dismal'],
                 'surprise': [
                     'sudden and shock and curious and amazing and dramatic and unexpected and awe and startling and amazingly and breathtaking and perplex'],
                 'disgust': [
                     'ugly and offensive and contempt and disgust and dislike and nausea and disdain and aversion and disgusting and intolerable and hateful'],
                 'fear': [
                     'anxiety and horror and panic and alarm and terrifying and agitation and apprehension and scare and insecurity and shudder and fright']}}
    else:
        hypothesis_emo_syns_LTOS = {
            2: {'noemo': ['others, no emotion'], 'joy': ['triumphant, gratitude'], 'anger': ['ire, hostility'],
                'sadness': ['sadness, dismal'], 'surprise': ['breathtaking, unforeseen'],
                'disgust': ['intolerable, offensive'], 'fear': ['shudder, horror']},
            3: {'noemo': ['others, no emotion'], 'joy': ['cheer, triumphant, bliss'],
                'anger': ['discontent, outrage, hostility'], 'sadness': ['grief, dismal, depression'],
                'surprise': ['shocked, unbelievable, unforeseen'], 'disgust': ['displeasure, ugly, offensive'],
                'fear': ['suspense, horror, terrifying']},
            4: {'noemo': ['others, no emotion'], 'joy': ['cheer, triumphant, joy, bliss'],
                'anger': ['indignation, outrage, hostility, provocation'],
                'sadness': ['sadness, grief, dismal, depression'],
                'surprise': ['shocked, unbelievable, amazing, unforeseen'],
                'disgust': ['ugly, bitter, nausea, offensive'], 'fear': ['suspense, fright, horror, terrifying']},
            5: {'noemo': ['others, no emotion'], 'joy': ['cheer, triumphant, achievement, pleasure, gratitude'],
                'anger': ['indignation, aversion, hostility, provocation, anger'],
                'sadness': ['sadness, grief, blues, tragic, depression'],
                'surprise': ['shocked, shock, awe, unbelievable, amazing'],
                'disgust': ['aversion, ugly, bitter, nausea, hateful'],
                'fear': ['fright, panic, insecurity, horror, chilling']}, 6: {'noemo': ['others, no emotion'], 'joy': [
                'cheer, triumphant, pleasure, gratitude, blessed, enchantment'], 'anger': [
                'indignation, outrage, aversion, hostility, fury, provocation'], 'sadness': [
                'sadly, sadness, grief, dismal, melancholy, pathetic'], 'surprise': [
                'shocked, shock, awe, unbelievable, amazing, sudden'], 'disgust': [
                'aversion, dislike, contempt, ugly, nausea, hateful'], 'fear': [
                'worry, fright, panic, insecurity, horror, terrifying']}, 7: {'noemo': ['others, no emotion'], 'joy': [
                'cheer, triumphant, achievement, pleasure, gratitude, blessed, enchantment'], 'anger': [
                'ire, indignation, aversion, hostility, annoyance, provocation, hatred'], 'sadness': [
                'sadly, sadness, grief, dismal, melancholy, blues, pathetic'], 'surprise': [
                'shocked, shock, awe, startling, abrupt, amazing, sudden'], 'disgust': [
                'aversion, dislike, contempt, ugly, vomiting, nausea, hateful'], 'fear': [
                'worry, fright, panic, insecurity, horror, anxiety, terrifying']}, 8: {'noemo': ['others, no emotion'],
                                                                                       'joy': [
                                                                                           'cheer, triumphant, achievement, pleasure, bliss, blessed, enchantment, ecstasy'],
                                                                                       'anger': [
                                                                                           'ire, indignation, aversion, hostility, annoyance, enraged, provocation, hatred'],
                                                                                       'sadness': [
                                                                                           'sadly, sadness, grief, dismal, melancholy, blues, pathetic, depression'],
                                                                                       'surprise': [
                                                                                           'shocked, curious, shock, astonishing, awe, abrupt, amazing, sudden'],
                                                                                       'disgust': [
                                                                                           'aversion, dislike, contempt, intolerable, ugly, nausea, offensive, hateful'],
                                                                                       'fear': [
                                                                                           'worry, scare, fright, panic, insecurity, horror, anxiety, terrifying']},
            9: {'noemo': ['others, no emotion'],
                'joy': ['cheer, triumphant, achievement, pleasure, joy, bliss, blessed, enchantment, ecstasy'],
                'anger': ['indignation, outrage, hostility, fury, animosity, provocation, resentment, hatred, malice'],
                'sadness': ['sadly, sadness, grief, dismal, despair, melancholy, blues, pathetic, depression'],
                'surprise': ['curious, shock, astonishing, awe, abrupt, amazing, breathtaking, unexpected, sudden'],
                'disgust': ['disdain, aversion, dislike, contempt, ugly, vomiting, disgusting, offensive, hateful'],
                'fear': ['apprehension, worry, scare, fright, panic, insecurity, horror, anxiety, terrifying']},
            10: {'noemo': ['others, no emotion'], 'joy': [
                'cheer, triumphant, awesome, achievement, pleasure, joy, bliss, blessed, enchantment, ecstasy'],
                 'anger': [
                     'ire, indignation, hostility, annoyance, enraged, animosity, provocation, rage, hatred, malice'],
                 'sadness': ['sadly, sadness, grief, dismal, despair, melancholy, blues, pathetic, tragic, depression'],
                 'surprise': [
                     'perplex, curious, shock, awe, unbelievable, amazing, breathtaking, unforeseen, unexpected, sudden'],
                 'disgust': [
                     'disdain, aversion, dislike, contempt, intolerable, ugly, nausea, disgusting, offensive, hateful'],
                 'fear': [
                     'shudder, agitation, apprehension, scare, fright, panic, insecurity, horror, anxiety, terrifying']},
            11: {'noemo': ['others, no emotion'], 'joy': [
                'cheer, delight, triumphant, awesome, achievement, pleasure, joy, bliss, blessed, enchantment, ecstasy'],
                 'anger': [
                     'indignation, outrage, hostility, annoyance, enraged, animosity, provocation, anger, rage, hatred, malice'],
                 'sadness': [
                     'sadly, sadness, grief, dismal, despair, melancholy, blues, pathetic, tragic, desperate, depression'],
                 'surprise': [
                     'perplex, curious, shock, awe, startling, amazingly, dramatic, amazing, breathtaking, unexpected, sudden'],
                 'disgust': [
                     'disdain, aversion, dislike, disgust, contempt, intolerable, ugly, nausea, disgusting, offensive, hateful'],
                 'fear': [
                     'shudder, alarm, agitation, apprehension, scare, fright, panic, insecurity, horror, anxiety, terrifying']}}
        hypothesis_emo_synspace_LTOS = {
            2: {'noemo': ['others no emotion'], 'joy': ['triumphant gratitude'], 'anger': ['ire hostility'],
                'sadness': ['sadness dismal'], 'surprise': ['breathtaking unforeseen'],
                'disgust': ['intolerable offensive'], 'fear': ['shudder horror']},
            3: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant bliss'],
                'anger': ['discontent outrage hostility'], 'sadness': ['grief dismal depression'],
                'surprise': ['shocked unbelievable unforeseen'], 'disgust': ['displeasure ugly offensive'],
                'fear': ['suspense horror terrifying']},
            4: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant joy bliss'],
                'anger': ['indignation outrage hostility provocation'], 'sadness': ['sadness grief dismal depression'],
                'surprise': ['shocked unbelievable amazing unforeseen'], 'disgust': ['ugly bitter nausea offensive'],
                'fear': ['suspense fright horror terrifying']},
            5: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant achievement pleasure gratitude'],
                'anger': ['indignation aversion hostility provocation anger'],
                'sadness': ['sadness grief blues tragic depression'],
                'surprise': ['shocked shock awe unbelievable amazing'],
                'disgust': ['aversion ugly bitter nausea hateful'],
                'fear': ['fright panic insecurity horror chilling']},
            6: {'noemo': ['others no emotion'], 'joy': ['cheer triumphant pleasure gratitude blessed enchantment'],
                'anger': ['indignation outrage aversion hostility fury provocation'],
                'sadness': ['sadly sadness grief dismal melancholy pathetic'],
                'surprise': ['shocked shock awe unbelievable amazing sudden'],
                'disgust': ['aversion dislike contempt ugly nausea hateful'],
                'fear': ['worry fright panic insecurity horror terrifying']}, 7: {'noemo': ['others no emotion'],
                                                                                  'joy': [
                                                                                      'cheer triumphant achievement pleasure gratitude blessed enchantment'],
                                                                                  'anger': [
                                                                                      'ire indignation aversion hostility annoyance provocation hatred'],
                                                                                  'sadness': [
                                                                                      'sadly sadness grief dismal melancholy blues pathetic'],
                                                                                  'surprise': [
                                                                                      'shocked shock awe startling abrupt amazing sudden'],
                                                                                  'disgust': [
                                                                                      'aversion dislike contempt ugly vomiting nausea hateful'],
                                                                                  'fear': [
                                                                                      'worry fright panic insecurity horror anxiety terrifying']},
            8: {'noemo': ['others no emotion'],
                'joy': ['cheer triumphant achievement pleasure bliss blessed enchantment ecstasy'],
                'anger': ['ire indignation aversion hostility annoyance enraged provocation hatred'],
                'sadness': ['sadly sadness grief dismal melancholy blues pathetic depression'],
                'surprise': ['shocked curious shock astonishing awe abrupt amazing sudden'],
                'disgust': ['aversion dislike contempt intolerable ugly nausea offensive hateful'],
                'fear': ['worry scare fright panic insecurity horror anxiety terrifying']},
            9: {'noemo': ['others no emotion'],
                'joy': ['cheer triumphant achievement pleasure joy bliss blessed enchantment ecstasy'],
                'anger': ['indignation outrage hostility fury animosity provocation resentment hatred malice'],
                'sadness': ['sadly sadness grief dismal despair melancholy blues pathetic depression'],
                'surprise': ['curious shock astonishing awe abrupt amazing breathtaking unexpected sudden'],
                'disgust': ['disdain aversion dislike contempt ugly vomiting disgusting offensive hateful'],
                'fear': ['apprehension worry scare fright panic insecurity horror anxiety terrifying']},
            10: {'noemo': ['others no emotion'],
                 'joy': ['cheer triumphant awesome achievement pleasure joy bliss blessed enchantment ecstasy'],
                 'anger': ['ire indignation hostility annoyance enraged animosity provocation rage hatred malice'],
                 'sadness': ['sadly sadness grief dismal despair melancholy blues pathetic tragic depression'],
                 'surprise': [
                     'perplex curious shock awe unbelievable amazing breathtaking unforeseen unexpected sudden'],
                 'disgust': ['disdain aversion dislike contempt intolerable ugly nausea disgusting offensive hateful'],
                 'fear': ['shudder agitation apprehension scare fright panic insecurity horror anxiety terrifying']},
            11: {'noemo': ['others no emotion'],
                 'joy': ['cheer delight triumphant awesome achievement pleasure joy bliss blessed enchantment ecstasy'],
                 'anger': [
                     'indignation outrage hostility annoyance enraged animosity provocation anger rage hatred malice'],
                 'sadness': [
                     'sadly sadness grief dismal despair melancholy blues pathetic tragic desperate depression'],
                 'surprise': [
                     'perplex curious shock awe startling amazingly dramatic amazing breathtaking unexpected sudden'],
                 'disgust': [
                     'disdain aversion dislike disgust contempt intolerable ugly nausea disgusting offensive hateful'],
                 'fear': [
                     'shudder alarm agitation apprehension scare fright panic insecurity horror anxiety terrifying']}}
        hypothesis_emo_synslash_LTOS = {
            2: {'noemo': ['others/ no emotion'], 'joy': ['triumphant/ gratitude'], 'anger': ['ire/ hostility'],
                'sadness': ['sadness/ dismal'], 'surprise': ['breathtaking/ unforeseen'],
                'disgust': ['intolerable/ offensive'], 'fear': ['shudder/ horror']},
            3: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ triumphant/ bliss'],
                'anger': ['discontent/ outrage/ hostility'], 'sadness': ['grief/ dismal/ depression'],
                'surprise': ['shocked/ unbelievable/ unforeseen'], 'disgust': ['displeasure/ ugly/ offensive'],
                'fear': ['suspense/ horror/ terrifying']},
            4: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ triumphant/ joy/ bliss'],
                'anger': ['indignation/ outrage/ hostility/ provocation'],
                'sadness': ['sadness/ grief/ dismal/ depression'],
                'surprise': ['shocked/ unbelievable/ amazing/ unforeseen'],
                'disgust': ['ugly/ bitter/ nausea/ offensive'], 'fear': ['suspense/ fright/ horror/ terrifying']},
            5: {'noemo': ['others/ no emotion'], 'joy': ['cheer/ triumphant/ achievement/ pleasure/ gratitude'],
                'anger': ['indignation/ aversion/ hostility/ provocation/ anger'],
                'sadness': ['sadness/ grief/ blues/ tragic/ depression'],
                'surprise': ['shocked/ shock/ awe/ unbelievable/ amazing'],
                'disgust': ['aversion/ ugly/ bitter/ nausea/ hateful'],
                'fear': ['fright/ panic/ insecurity/ horror/ chilling']}, 6: {'noemo': ['others/ no emotion'], 'joy': [
                'cheer/ triumphant/ pleasure/ gratitude/ blessed/ enchantment'], 'anger': [
                'indignation/ outrage/ aversion/ hostility/ fury/ provocation'], 'sadness': [
                'sadly/ sadness/ grief/ dismal/ melancholy/ pathetic'], 'surprise': [
                'shocked/ shock/ awe/ unbelievable/ amazing/ sudden'], 'disgust': [
                'aversion/ dislike/ contempt/ ugly/ nausea/ hateful'], 'fear': [
                'worry/ fright/ panic/ insecurity/ horror/ terrifying']}, 7: {'noemo': ['others/ no emotion'], 'joy': [
                'cheer/ triumphant/ achievement/ pleasure/ gratitude/ blessed/ enchantment'], 'anger': [
                'ire/ indignation/ aversion/ hostility/ annoyance/ provocation/ hatred'], 'sadness': [
                'sadly/ sadness/ grief/ dismal/ melancholy/ blues/ pathetic'], 'surprise': [
                'shocked/ shock/ awe/ startling/ abrupt/ amazing/ sudden'], 'disgust': [
                'aversion/ dislike/ contempt/ ugly/ vomiting/ nausea/ hateful'], 'fear': [
                'worry/ fright/ panic/ insecurity/ horror/ anxiety/ terrifying']}, 8: {'noemo': ['others/ no emotion'],
                                                                                       'joy': [
                                                                                           'cheer/ triumphant/ achievement/ pleasure/ bliss/ blessed/ enchantment/ ecstasy'],
                                                                                       'anger': [
                                                                                           'ire/ indignation/ aversion/ hostility/ annoyance/ enraged/ provocation/ hatred'],
                                                                                       'sadness': [
                                                                                           'sadly/ sadness/ grief/ dismal/ melancholy/ blues/ pathetic/ depression'],
                                                                                       'surprise': [
                                                                                           'shocked/ curious/ shock/ astonishing/ awe/ abrupt/ amazing/ sudden'],
                                                                                       'disgust': [
                                                                                           'aversion/ dislike/ contempt/ intolerable/ ugly/ nausea/ offensive/ hateful'],
                                                                                       'fear': [
                                                                                           'worry/ scare/ fright/ panic/ insecurity/ horror/ anxiety/ terrifying']},
            9: {'noemo': ['others/ no emotion'],
                'joy': ['cheer/ triumphant/ achievement/ pleasure/ joy/ bliss/ blessed/ enchantment/ ecstasy'],
                'anger': ['indignation/ outrage/ hostility/ fury/ animosity/ provocation/ resentment/ hatred/ malice'],
                'sadness': ['sadly/ sadness/ grief/ dismal/ despair/ melancholy/ blues/ pathetic/ depression'],
                'surprise': ['curious/ shock/ astonishing/ awe/ abrupt/ amazing/ breathtaking/ unexpected/ sudden'],
                'disgust': ['disdain/ aversion/ dislike/ contempt/ ugly/ vomiting/ disgusting/ offensive/ hateful'],
                'fear': ['apprehension/ worry/ scare/ fright/ panic/ insecurity/ horror/ anxiety/ terrifying']},
            10: {'noemo': ['others/ no emotion'], 'joy': [
                'cheer/ triumphant/ awesome/ achievement/ pleasure/ joy/ bliss/ blessed/ enchantment/ ecstasy'],
                 'anger': [
                     'ire/ indignation/ hostility/ annoyance/ enraged/ animosity/ provocation/ rage/ hatred/ malice'],
                 'sadness': ['sadly/ sadness/ grief/ dismal/ despair/ melancholy/ blues/ pathetic/ tragic/ depression'],
                 'surprise': [
                     'perplex/ curious/ shock/ awe/ unbelievable/ amazing/ breathtaking/ unforeseen/ unexpected/ sudden'],
                 'disgust': [
                     'disdain/ aversion/ dislike/ contempt/ intolerable/ ugly/ nausea/ disgusting/ offensive/ hateful'],
                 'fear': [
                     'shudder/ agitation/ apprehension/ scare/ fright/ panic/ insecurity/ horror/ anxiety/ terrifying']},
            11: {'noemo': ['others/ no emotion'], 'joy': [
                'cheer/ delight/ triumphant/ awesome/ achievement/ pleasure/ joy/ bliss/ blessed/ enchantment/ ecstasy'],
                 'anger': [
                     'indignation/ outrage/ hostility/ annoyance/ enraged/ animosity/ provocation/ anger/ rage/ hatred/ malice'],
                 'sadness': [
                     'sadly/ sadness/ grief/ dismal/ despair/ melancholy/ blues/ pathetic/ tragic/ desperate/ depression'],
                 'surprise': [
                     'perplex/ curious/ shock/ awe/ startling/ amazingly/ dramatic/ amazing/ breathtaking/ unexpected/ sudden'],
                 'disgust': [
                     'disdain/ aversion/ dislike/ disgust/ contempt/ intolerable/ ugly/ nausea/ disgusting/ offensive/ hateful'],
                 'fear': [
                     'shudder/ alarm/ agitation/ apprehension/ scare/ fright/ panic/ insecurity/ horror/ anxiety/ terrifying']}}
        hypothesis_emo_synsand_LTOS = {
            2: {'noemo': ['others and no emotion'], 'joy': ['triumphant and gratitude'], 'anger': ['ire and hostility'],
                'sadness': ['sadness and dismal'], 'surprise': ['breathtaking and unforeseen'],
                'disgust': ['intolerable and offensive'], 'fear': ['shudder and horror']},
            3: {'noemo': ['others and no emotion'], 'joy': ['cheer and triumphant and bliss'],
                'anger': ['discontent and outrage and hostility'], 'sadness': ['grief and dismal and depression'],
                'surprise': ['shocked and unbelievable and unforeseen'],
                'disgust': ['displeasure and ugly and offensive'], 'fear': ['suspense and horror and terrifying']},
            4: {'noemo': ['others and no emotion'], 'joy': ['cheer and triumphant and joy and bliss'],
                'anger': ['indignation and outrage and hostility and provocation'],
                'sadness': ['sadness and grief and dismal and depression'],
                'surprise': ['shocked and unbelievable and amazing and unforeseen'],
                'disgust': ['ugly and bitter and nausea and offensive'],
                'fear': ['suspense and fright and horror and terrifying']}, 5: {'noemo': ['others and no emotion'],
                                                                                'joy': [
                                                                                    'cheer and triumphant and achievement and pleasure and gratitude'],
                                                                                'anger': [
                                                                                    'indignation and aversion and hostility and provocation and anger'],
                                                                                'sadness': [
                                                                                    'sadness and grief and blues and tragic and depression'],
                                                                                'surprise': [
                                                                                    'shocked and shock and awe and unbelievable and amazing'],
                                                                                'disgust': [
                                                                                    'aversion and ugly and bitter and nausea and hateful'],
                                                                                'fear': [
                                                                                    'fright and panic and insecurity and horror and chilling']},
            6: {'noemo': ['others and no emotion'],
                'joy': ['cheer and triumphant and pleasure and gratitude and blessed and enchantment'],
                'anger': ['indignation and outrage and aversion and hostility and fury and provocation'],
                'sadness': ['sadly and sadness and grief and dismal and melancholy and pathetic'],
                'surprise': ['shocked and shock and awe and unbelievable and amazing and sudden'],
                'disgust': ['aversion and dislike and contempt and ugly and nausea and hateful'],
                'fear': ['worry and fright and panic and insecurity and horror and terrifying']},
            7: {'noemo': ['others and no emotion'],
                'joy': ['cheer and triumphant and achievement and pleasure and gratitude and blessed and enchantment'],
                'anger': ['ire and indignation and aversion and hostility and annoyance and provocation and hatred'],
                'sadness': ['sadly and sadness and grief and dismal and melancholy and blues and pathetic'],
                'surprise': ['shocked and shock and awe and startling and abrupt and amazing and sudden'],
                'disgust': ['aversion and dislike and contempt and ugly and vomiting and nausea and hateful'],
                'fear': ['worry and fright and panic and insecurity and horror and anxiety and terrifying']},
            8: {'noemo': ['others and no emotion'], 'joy': [
                'cheer and triumphant and achievement and pleasure and bliss and blessed and enchantment and ecstasy'],
                'anger': [
                    'ire and indignation and aversion and hostility and annoyance and enraged and provocation and hatred'],
                'sadness': [
                    'sadly and sadness and grief and dismal and melancholy and blues and pathetic and depression'],
                'surprise': ['shocked and curious and shock and astonishing and awe and abrupt and amazing and sudden'],
                'disgust': [
                    'aversion and dislike and contempt and intolerable and ugly and nausea and offensive and hateful'],
                'fear': ['worry and scare and fright and panic and insecurity and horror and anxiety and terrifying']},
            9: {'noemo': ['others and no emotion'], 'joy': [
                'cheer and triumphant and achievement and pleasure and joy and bliss and blessed and enchantment and ecstasy'],
                'anger': [
                    'indignation and outrage and hostility and fury and animosity and provocation and resentment and hatred and malice'],
                'sadness': [
                    'sadly and sadness and grief and dismal and despair and melancholy and blues and pathetic and depression'],
                'surprise': [
                    'curious and shock and astonishing and awe and abrupt and amazing and breathtaking and unexpected and sudden'],
                'disgust': [
                    'disdain and aversion and dislike and contempt and ugly and vomiting and disgusting and offensive and hateful'],
                'fear': [
                    'apprehension and worry and scare and fright and panic and insecurity and horror and anxiety and terrifying']},
            10: {'noemo': ['others and no emotion'], 'joy': [
                'cheer and triumphant and awesome and achievement and pleasure and joy and bliss and blessed and enchantment and ecstasy'],
                 'anger': [
                     'ire and indignation and hostility and annoyance and enraged and animosity and provocation and rage and hatred and malice'],
                 'sadness': [
                     'sadly and sadness and grief and dismal and despair and melancholy and blues and pathetic and tragic and depression'],
                 'surprise': [
                     'perplex and curious and shock and awe and unbelievable and amazing and breathtaking and unforeseen and unexpected and sudden'],
                 'disgust': [
                     'disdain and aversion and dislike and contempt and intolerable and ugly and nausea and disgusting and offensive and hateful'],
                 'fear': [
                     'shudder and agitation and apprehension and scare and fright and panic and insecurity and horror and anxiety and terrifying']},
            11: {'noemo': ['others and no emotion'], 'joy': [
                'cheer and delight and triumphant and awesome and achievement and pleasure and joy and bliss and blessed and enchantment and ecstasy'],
                 'anger': [
                     'indignation and outrage and hostility and annoyance and enraged and animosity and provocation and anger and rage and hatred and malice'],
                 'sadness': [
                     'sadly and sadness and grief and dismal and despair and melancholy and blues and pathetic and tragic and desperate and depression'],
                 'surprise': [
                     'perplex and curious and shock and awe and startling and amazingly and dramatic and amazing and breathtaking and unexpected and sudden'],
                 'disgust': [
                     'disdain and aversion and dislike and disgust and contempt and intolerable and ugly and nausea and disgusting and offensive and hateful'],
                 'fear': [
                     'shudder and alarm and agitation and apprehension and scare and fright and panic and insecurity and horror and anxiety and terrifying']}}

    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 12)
    for dataname in datasetnames:
        hypothesis = f'./data/hypothesis/hypothesis_final/hypothesis_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = './data/' + dataname.upper() + '/' + dataname.lower() + '_test.csv'
                        rows = []
                        with open(train) as f:
                            csv_read = csv.reader(f)
                            for row in csv_read:
                                label = ['joy', 'anger', 'sadness', 'surprise', 'disgust', 'noemo', 'fear']
                                for l in label:
                                    with open(hypothesis) as tf:
                                        csv_temp = csv.reader(tf)
                                        for tem in csv_temp:
                                            if sprompt == 'syns':
                                                hypothesis_emo_s = hypothesis_emo_syns_LTOS[num]
                                            elif sprompt == 'synspace':
                                                hypothesis_emo_s = hypothesis_emo_synspace_LTOS[num]
                                            elif sprompt == 'synslash':
                                                hypothesis_emo_s = hypothesis_emo_synslash_LTOS[num]
                                            elif sprompt == 'synsand':
                                                hypothesis_emo_s = hypothesis_emo_synsand_LTOS[num]
                                            else:
                                                print('error')
                                                exit()
                                            st = []
                                            st.append(row[0])
                                            truetem = tem[0].replace('M', hypothesis_emo_s[l][0])
                                            st.append(truetem)
                                            if l == row[1]:
                                                st.append('entailment')
                                            else:
                                                st.append('contradiction')
                                            st.append(row[1])
                                            st.append(l)
                                            rows.append(st)

                        with open(modifiedfile, 'w', newline='') as f:
                            f_csv = csv.writer(f)
                            f_csv.writerows(rows)
                        combine(modifiedfile, savefile)

                    else:
                        for n in range(5):
                            savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail_' + str(n) + '.csv'
                            modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '_' + str(n) + '.csv'

                            train = './data/' + dataname.upper() + '/' + dataname.lower() + 'select_' + td + '_' + str(
                                n) + '.csv'
                            rows = []
                            with open(train) as f:
                                csv_read = csv.reader(f)
                                for row in csv_read:
                                    with open(hypothesis) as tf:
                                        csv_temp = csv.reader(tf)
                                        for tem in csv_temp:
                                            if sprompt == 'syns':
                                                hypothesis_emo_s = hypothesis_emo_syns_LTOS[num]
                                            elif sprompt == 'synspace':
                                                hypothesis_emo_s = hypothesis_emo_synspace_LTOS[num]
                                            elif sprompt == 'synslash':
                                                hypothesis_emo_s = hypothesis_emo_synslash_LTOS[num]
                                            elif sprompt == 'synsand':
                                                hypothesis_emo_s = hypothesis_emo_synsand_LTOS[num]
                                            else:
                                                print('error')
                                                exit()
                                            label = ['joy', 'anger', 'sadness', 'surprise', 'disgust', 'noemo',
                                                     'fear']
                                            st = []
                                            st.append(row[0])
                                            truetem = tem[0].replace('M', hypothesis_emo_s[row[1]][0])
                                            st.append(truetem)
                                            st.append('entailment')
                                            st.append(row[1])
                                            st.append(row[1])
                                            rows.append(st)
                                            label.remove(row[1])
                                            falselabelselect = sample(label, 1)
                                            for falselabel in falselabelselect:
                                                st = []
                                                st.append(row[0])
                                                falsetem = tem[0].replace("M", hypothesis_emo_s[falselabel][0])
                                                st.append(falsetem)
                                                st.append('contradiction')
                                                st.append(row[1])
                                                st.append(falselabel)
                                                rows.append(st)
                            with open(savefile, 'w', newline='') as f:
                                f_csv = csv.writer(f)
                                f_csv.writerows(rows)
                            combine(modifiedfile, savefile)

if __name__ == '__main__':
    knowledge=['freq','entail']
    for k in knowledge:
        mainaman(k)
        mainmeld(k)
