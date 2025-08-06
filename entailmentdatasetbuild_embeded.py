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
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num} \n')
                    if td == 'test':
                        for n in range(5):
                            savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str( num) +  '_' + sprompt+'_' + td +'entail_'+str(n)+'.csv'
                            modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str( num) +  '_' + sprompt+'_' + td +'_'+str(n)+'.csv'
                            train = '32-shot-dataset/er/' + dataname.upper() + '/' + dataname.lower() +'select_'+td+'02_'+str(n)+'.csv'
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
                            train = '32-shot-dataset/er/' + dataname.upper() + '/' + dataname.lower() + 'select_' + td + '_' + str(
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
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = '32-shot-dataset/er/' + dataname.upper() + '/' + dataname.lower() + '_test.csv'
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

                            train = '32-shot-dataset/sa/CR/' + dataname.lower() + '_select_' + td + '_' + str(
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




def maintrec(k):
    datasetnames = [
        'trec'
    ]
    traindev = [
        'train', 'dev',
        'test']
    if k == 'freq':
        hypothesis_emo_syns_LTOS = {
            2: {'entity': ['method, substance'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['manner, description'], 'human': ['individual, title'],
                'location': ['country, location'], 'number': ['weight, rank']},
            3: {'entity': ['body, event, substance'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['reason, manner, description'], 'human': ['group, organization, title'],
                'location': ['state, city, location'], 'number': ['number, distance, date']},
            4: {'entity': ['body, event, color, substance'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['reason, manner, definition, description'],
                'human': ['group, organization, persons, title'], 'location': ['state, country, location, mountain'],
                'number': ['number, percent, distance, date']}, 5: {'entity': ['body, method, event, color, substance'],
                                                                    'abbreviation': [
                                                                        'abbreviation, expression abbreviated'],
                                                                    'description': [
                                                                        'reason, action, manner, definition, description'],
                                                                    'human': [
                                                                        'individual, organization, persons, description, title'],
                                                                    'location': [
                                                                        'state, country, city, location, mountain'],
                                                                    'number': [
                                                                        'number, percent, distance, date, code']}}



        hypothesis_emo_synspace_LTOS = {
            2: {'entity': ['method substance'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['manner description'], 'human': ['individual title'], 'location': ['country location'],
                'number': ['weight rank']},
            3: {'entity': ['body event substance'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['reason manner description'], 'human': ['group organization title'],
                'location': ['state city location'], 'number': ['number distance date']},
            4: {'entity': ['body event color substance'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['reason manner definition description'], 'human': ['group organization persons title'],
                'location': ['state country location mountain'], 'number': ['number percent distance date']},
            5: {'entity': ['body method event color substance'],
                'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['reason action manner definition description'],
                'human': ['individual organization persons description title'],
                'location': ['state country city location mountain'], 'number': ['number percent distance date code']}}



        hypothesis_emo_synslash_LTOS = {
            2: {'entity': ['method/ substance'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['manner/ description'], 'human': ['individual/ title'],
                'location': ['country/ location'], 'number': ['weight/ rank']},
            3: {'entity': ['body/ event/ substance'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['reason/ manner/ description'], 'human': ['group/ organization/ title'],
                'location': ['state/ city/ location'], 'number': ['number/ distance/ date']},
            4: {'entity': ['body/ event/ color/ substance'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['reason/ manner/ definition/ description'],
                'human': ['group/ organization/ persons/ title'], 'location': ['state/ country/ location/ mountain'],
                'number': ['number/ percent/ distance/ date']}, 5: {'entity': ['body/ method/ event/ color/ substance'],
                                                                    'abbreviation': [
                                                                        'abbreviation/ expression abbreviated'],
                                                                    'description': [
                                                                        'reason/ action/ manner/ definition/ description'],
                                                                    'human': [
                                                                        'individual/ organization/ persons/ description/ title'],
                                                                    'location': [
                                                                        'state/ country/ city/ location/ mountain'],
                                                                    'number': [
                                                                        'number/ percent/ distance/ date/ code']}}



        hypothesis_emo_synsand_LTOS = {
            2: {'entity': ['method and substance'], 'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['manner and description'], 'human': ['individual and title'],
                'location': ['country and location'], 'number': ['weight and rank']},
            3: {'entity': ['body and event and substance'], 'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['reason and manner and description'], 'human': ['group and organization and title'],
                'location': ['state and city and location'], 'number': ['number and distance and date']},
            4: {'entity': ['body and event and color and substance'],
                'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['reason and manner and definition and description'],
                'human': ['group and organization and persons and title'],
                'location': ['state and country and location and mountain'],
                'number': ['number and percent and distance and date']},
            5: {'entity': ['body and method and event and color and substance'],
                'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['reason and action and manner and definition and description'],
                'human': ['individual and organization and persons and description and title'],
                'location': ['state and country and city and location and mountain'],
                'number': ['number and percent and distance and date and code']}}


    else:
        hypothesis_emo_syns_LTOS = {
            2: {'entity': ['substance, method'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['manner, description'], 'human': ['individual, title'],
                'location': ['location, country'], 'number': ['rank, weight']},
            3: {'entity': ['substance, event, body'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['reason, manner, description'], 'human': ['title, group, organization'],
                'location': ['location, city, state'], 'number': ['number, date, distance']},
            4: {'entity': ['substance, event, body, color'], 'abbreviation': ['abbreviation, expression abbreviated'],
                'description': ['definition, reason, manner, description'],
                'human': ['persons, title, group, organization'], 'location': ['location, country, state, mountain'],
                'number': ['number, date, distance, percent']}, 5: {'entity': ['substance, event, method, body, color'],
                                                                    'abbreviation': [
                                                                        'abbreviation, expression abbreviated'],
                                                                    'description': [
                                                                        'definition, reason, manner, description, action'],
                                                                    'human': [
                                                                        'individual, persons, description, title, organization'],
                                                                    'location': [
                                                                        'location, country, city, state, mountain'],
                                                                    'number': [
                                                                        'number, date, distance, code, percent']}}


        hypothesis_emo_synspace_LTOS = {
            2: {'entity': ['substance method'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['manner description'], 'human': ['individual title'], 'location': ['location country'],
                'number': ['rank weight']},
            3: {'entity': ['substance event body'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['reason manner description'], 'human': ['title group organization'],
                'location': ['location city state'], 'number': ['number date distance']},
            4: {'entity': ['substance event body color'], 'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['definition reason manner description'], 'human': ['persons title group organization'],
                'location': ['location country state mountain'], 'number': ['number date distance percent']},
            5: {'entity': ['substance event method body color'],
                'abbreviation': ['abbreviation expression abbreviated'],
                'description': ['definition reason manner description action'],
                'human': ['individual persons description title organization'],
                'location': ['location country city state mountain'], 'number': ['number date distance code percent']}}

        hypothesis_emo_synslash_LTOS = {
            2: {'entity': ['substance/ method'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['manner/ description'], 'human': ['individual/ title'],
                'location': ['location/ country'], 'number': ['rank/ weight']},
            3: {'entity': ['substance/ event/ body'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['reason/ manner/ description'], 'human': ['title/ group/ organization'],
                'location': ['location/ city/ state'], 'number': ['number/ date/ distance']},
            4: {'entity': ['substance/ event/ body/ color'], 'abbreviation': ['abbreviation/ expression abbreviated'],
                'description': ['definition/ reason/ manner/ description'],
                'human': ['persons/ title/ group/ organization'], 'location': ['location/ country/ state/ mountain'],
                'number': ['number/ date/ distance/ percent']}, 5: {'entity': ['substance/ event/ method/ body/ color'],
                                                                    'abbreviation': [
                                                                        'abbreviation/ expression abbreviated'],
                                                                    'description': [
                                                                        'definition/ reason/ manner/ description/ action'],
                                                                    'human': [
                                                                        'individual/ persons/ description/ title/ organization'],
                                                                    'location': [
                                                                        'location/ country/ city/ state/ mountain'],
                                                                    'number': [
                                                                        'number/ date/ distance/ code/ percent']}}



        hypothesis_emo_synsand_LTOS = {
            2: {'entity': ['substance and method'], 'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['manner and description'], 'human': ['individual and title'],
                'location': ['location and country'], 'number': ['rank and weight']},
            3: {'entity': ['substance and event and body'], 'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['reason and manner and description'], 'human': ['title and group and organization'],
                'location': ['location and city and state'], 'number': ['number and date and distance']},
            4: {'entity': ['substance and event and body and color'],
                'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['definition and reason and manner and description'],
                'human': ['persons and title and group and organization'],
                'location': ['location and country and state and mountain'],
                'number': ['number and date and distance and percent']},
            5: {'entity': ['substance and event and method and body and color'],
                'abbreviation': ['abbreviation and expression abbreviated'],
                'description': ['definition and reason and manner and description and action'],
                'human': ['individual and persons and description and title and organization'],
                'location': ['location and country and city and state and mountain'],
                'number': ['number and date and distance and code and percent']}}



    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 6)
    for dataname in datasetnames:
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = '32-shot-dataset/trec/' + dataname.lower() + '_test.csv'
                        rows = []
                        with open(train) as f:
                            csv_read = csv.reader(f)
                            for row in csv_read:
                                label = ['abbreviation',
                                         'entity',
                                         'description',
                                         'human',
                                         'location',
                                         'number']
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

                            train = '32-shot-dataset/trec/' + dataname.lower() + 'select_' + td + '_' + str(
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
                                            label = ['abbreviation',
                                         'entity',
                                         'description',
                                         'human',
                                         'location',
                                         'number']
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



def mainsst2(k):
    datasetnames = [
        'sst2'
    ]
    traindev = [
        'train', 'dev',
        'test']
    if k == 'freq':
        hypothesis_emo_syns_LTOS =  {2: {'positive': ['encouraging, redemption'], 'negative': ['worst, sneaky']},
                          3: {'positive': ['encouraging, constructive, proactive'],
                              'negative': ['disappointed, needy, sneaky']},
                          4: {'positive': ['relief, encouraging, constructive, proactive'],
                              'negative': ['attack, disappointed, needy, sneaky']},
                          5: {'positive': ['relief, pride, defeat, encouraging, constructive'],
                              'negative': ['attack, unsure, naughty, divisive, sneaky']},
                          6: {'positive': ['relief, pride, defeat, paradise, personalized, truthful'],
                              'negative': ['attack, broken, damage, waning, divisive, sneaky']},
                          7: {'positive': ['gold, relief, pride, defeat, paradise, personalized, truthful'],
                              'negative': ['attack, damage, racism, fearful, lied, sneaky, bashing']}, 8: {
        'positive': ['gold, relief, pride, grateful, defeat, skilled, ecstatic, renaissance'],
        'negative': ['attack, damage, racism, impose, opponent, fearful, lied, bashing']}, 9: {
        'positive': ['freedom, protection, gold, pride, grateful, defeat, skilled, ecstatic, renaissance'],
        'negative': ['attack, damage, rage, impose, opponent, complain, devastated, naughty, haunting']}, 10: {
        'positive': [
            'clearly, freedom, protection, gold, pride, defeat, dazzling, personalized, vigilance, ecstatic'],
        'negative': ['attack, damage, fuck, rage, disappointed, impose, opponent, complain, hateful, waning']},
                          11: {'positive': [
                              'freedom, protection, gold, fun, pride, eager, defeat, constructive, elegance, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, fuck, rage, assault, disappointed, impose, opponent, complain, hateful, waning']},
                          12: {'positive': [
                              'clearly, freedom, protection, gold, magic, skill, pride, defeat, dazzling, personalized, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          13: {'positive': [
                              'freedom, protection, gold, magic, skill, pride, defeat, intimate, gains, dazzling, personalized, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, darkness, fuck, assault, disappointed, racism, impose, opponent, complain, falsehood, insensitive, waning']},
                          14: {'positive': [
                              'smile, freedom, protection, popular, gold, magic, skill, pride, honor, defeat, educated, skilled, constructive, unforgettable'],
                              'negative': [
                                  'negative, attack, damage, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          15: {'positive': [
                              'smile, freedom, protection, popular, gold, magic, skill, pride, defeat, educated, skilled, constructive, proactive, vigilance, unforgettable'],
                              'negative': [
                                  'negative, attack, damage, noise, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          16: {'positive': [
                              'patient, smile, freedom, protection, popular, gold, magic, skill, pride, grateful, eager, defeat, delicate, proactive, salute, personalized'],
                              'negative': [
                                  'negative, attack, damage, absence, darkness, worried, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, extremist']},
                          17: {'positive': [
                              'freedom, protection, popular, gold, relief, magic, skill, pride, honor, defeat, gains, skilled, fantastic, constructive, tempting, proactive, unforgettable'],
                              'negative': [
                                  'attack, broken, damage, noise, darkness, shit, fuck, assault, impose, opponent, bruised, hateful, insensitive, scandals, satirical, discouraging, bashing']},
                          18: {'positive': [
                              'patient, clearly, freedom, protection, gold, relief, magic, skill, pride, defeat, educated, gains, skilled, proactive, salute, charismatic, meticulously, unforgettable'],
                              'negative': [
                                  'attack, damage, noise, darkness, worst, shit, fuck, warned, disappointed, impose, opponent, restriction, complain, disagree, siege, hateful, scandals, bashing']},
                          19: {'positive': [
                              'freedom, protection, gold, spiritual, liked, relief, magic, skill, pride, grateful, succeeded, defeat, gains, advocate, fantastic, wins, paradise, proactive, humorous'],
                              'negative': [
                                  'negative, attack, broken, damage, noise, darkness, shit, fuck, rage, impose, nonsense, opponent, incomplete, disagree, poorer, rogue, sabotage, insensitive, breakup']},
                          20: {'positive': [
                              'patient, smile, clearly, freedom, protection, gold, relief, magic, stronger, skill, pride, defeat, educated, merry, fiery, brighter, proactive, salute, personalized, inspirational'],
                              'negative': [
                                  'negative, attack, damage, noise, darkness, limit, shit, fuck, disappointed, impose, rape, opponent, rude, complain, siege, rogue, hateful, insensitive, scandals, bashing']}}



        hypothesis_emo_synspace_LTOS =  {2: {'positive': ['encouraging redemption'], 'negative': ['worst sneaky']},
                              3: {'positive': ['encouraging constructive proactive'],
                                  'negative': ['disappointed needy sneaky']},
                              4: {'positive': ['relief encouraging constructive proactive'],
                                  'negative': ['attack disappointed needy sneaky']},
                              5: {'positive': ['relief pride defeat encouraging constructive'],
                                  'negative': ['attack unsure naughty divisive sneaky']},
                              6: {'positive': ['relief pride defeat paradise personalized truthful'],
                                  'negative': ['attack broken damage waning divisive sneaky']},
                              7: {'positive': ['gold relief pride defeat paradise personalized truthful'],
                                  'negative': ['attack damage racism fearful lied sneaky bashing']}, 8: {
        'positive': ['gold relief pride grateful defeat skilled ecstatic renaissance'],
        'negative': ['attack damage racism impose opponent fearful lied bashing']}, 9: {
        'positive': ['freedom protection gold pride grateful defeat skilled ecstatic renaissance'],
        'negative': ['attack damage rage impose opponent complain devastated naughty haunting']}, 10: {
        'positive': ['clearly freedom protection gold pride defeat dazzling personalized vigilance ecstatic'],
        'negative': ['attack damage fuck rage disappointed impose opponent complain hateful waning']}, 11: {
        'positive': ['freedom protection gold fun pride eager defeat constructive elegance vigilance ecstatic'],
        'negative': ['attack damage fuck rage assault disappointed impose opponent complain hateful waning']},
                              12: {'positive': [
                                  'clearly freedom protection gold magic skill pride defeat dazzling personalized vigilance ecstatic'],
                                  'negative': [
                                      'attack damage fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              13: {'positive': [
                                  'freedom protection gold magic skill pride defeat intimate gains dazzling personalized vigilance ecstatic'],
                                  'negative': [
                                      'attack damage darkness fuck assault disappointed racism impose opponent complain falsehood insensitive waning']},
                              14: {'positive': [
                                  'smile freedom protection popular gold magic skill pride honor defeat educated skilled constructive unforgettable'],
                                  'negative': [
                                      'negative attack damage shit fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              15: {'positive': [
                                  'smile freedom protection popular gold magic skill pride defeat educated skilled constructive proactive vigilance unforgettable'],
                                  'negative': [
                                      'negative attack damage noise shit fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              16: {'positive': [
                                  'patient smile freedom protection popular gold magic skill pride grateful eager defeat delicate proactive salute personalized'],
                                  'negative': [
                                      'negative attack damage absence darkness worried shit fuck disappointed impose opponent complain disagree haunting scandals extremist']},
                              17: {'positive': [
                                  'freedom protection popular gold relief magic skill pride honor defeat gains skilled fantastic constructive tempting proactive unforgettable'],
                                  'negative': [
                                      'attack broken damage noise darkness shit fuck assault impose opponent bruised hateful insensitive scandals satirical discouraging bashing']},
                              18: {'positive': [
                                  'patient clearly freedom protection gold relief magic skill pride defeat educated gains skilled proactive salute charismatic meticulously unforgettable'],
                                  'negative': [
                                      'attack damage noise darkness worst shit fuck warned disappointed impose opponent restriction complain disagree siege hateful scandals bashing']},
                              19: {'positive': [
                                  'freedom protection gold spiritual liked relief magic skill pride grateful succeeded defeat gains advocate fantastic wins paradise proactive humorous'],
                                  'negative': [
                                      'negative attack broken damage noise darkness shit fuck rage impose nonsense opponent incomplete disagree poorer rogue sabotage insensitive breakup']},
                              20: {'positive': [
                                  'patient smile clearly freedom protection gold relief magic stronger skill pride defeat educated merry fiery brighter proactive salute personalized inspirational'],
                                  'negative': [
                                      'negative attack damage noise darkness limit shit fuck disappointed impose rape opponent rude complain siege rogue hateful insensitive scandals bashing']}}



        hypothesis_emo_synslash_LTOS = {2: {'positive': ['encouraging/ redemption'], 'negative': ['worst/ sneaky']},
                              3: {'positive': ['encouraging/ constructive/ proactive'],
                                  'negative': ['disappointed/ needy/ sneaky']},
                              4: {'positive': ['relief/ encouraging/ constructive/ proactive'],
                                  'negative': ['attack/ disappointed/ needy/ sneaky']},
                              5: {'positive': ['relief/ pride/ defeat/ encouraging/ constructive'],
                                  'negative': ['attack/ unsure/ naughty/ divisive/ sneaky']},
                              6: {'positive': ['relief/ pride/ defeat/ paradise/ personalized/ truthful'],
                                  'negative': ['attack/ broken/ damage/ waning/ divisive/ sneaky']},
                              7: {'positive': ['gold/ relief/ pride/ defeat/ paradise/ personalized/ truthful'],
                                  'negative': ['attack/ damage/ racism/ fearful/ lied/ sneaky/ bashing']}, 8: {
        'positive': ['gold/ relief/ pride/ grateful/ defeat/ skilled/ ecstatic/ renaissance'],
        'negative': ['attack/ damage/ racism/ impose/ opponent/ fearful/ lied/ bashing']}, 9: {
        'positive': ['freedom/ protection/ gold/ pride/ grateful/ defeat/ skilled/ ecstatic/ renaissance'],
        'negative': ['attack/ damage/ rage/ impose/ opponent/ complain/ devastated/ naughty/ haunting']}, 10: {
        'positive': [
            'clearly/ freedom/ protection/ gold/ pride/ defeat/ dazzling/ personalized/ vigilance/ ecstatic'],
        'negative': ['attack/ damage/ fuck/ rage/ disappointed/ impose/ opponent/ complain/ hateful/ waning']},
                              11: {'positive': [
                                  'freedom/ protection/ gold/ fun/ pride/ eager/ defeat/ constructive/ elegance/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ fuck/ rage/ assault/ disappointed/ impose/ opponent/ complain/ hateful/ waning']},
                              12: {'positive': [
                                  'clearly/ freedom/ protection/ gold/ magic/ skill/ pride/ defeat/ dazzling/ personalized/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              13: {'positive': [
                                  'freedom/ protection/ gold/ magic/ skill/ pride/ defeat/ intimate/ gains/ dazzling/ personalized/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ darkness/ fuck/ assault/ disappointed/ racism/ impose/ opponent/ complain/ falsehood/ insensitive/ waning']},
                              14: {'positive': [
                                  'smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ honor/ defeat/ educated/ skilled/ constructive/ unforgettable'],
                                  'negative': [
                                      'negative/ attack/ damage/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              15: {'positive': [
                                  'smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ defeat/ educated/ skilled/ constructive/ proactive/ vigilance/ unforgettable'],
                                  'negative': [
                                      'negative/ attack/ damage/ noise/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              16: {'positive': [
                                  'patient/ smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ grateful/ eager/ defeat/ delicate/ proactive/ salute/ personalized'],
                                  'negative': [
                                      'negative/ attack/ damage/ absence/ darkness/ worried/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ extremist']},
                              17: {'positive': [
                                  'freedom/ protection/ popular/ gold/ relief/ magic/ skill/ pride/ honor/ defeat/ gains/ skilled/ fantastic/ constructive/ tempting/ proactive/ unforgettable'],
                                  'negative': [
                                      'attack/ broken/ damage/ noise/ darkness/ shit/ fuck/ assault/ impose/ opponent/ bruised/ hateful/ insensitive/ scandals/ satirical/ discouraging/ bashing']},
                              18: {'positive': [
                                  'patient/ clearly/ freedom/ protection/ gold/ relief/ magic/ skill/ pride/ defeat/ educated/ gains/ skilled/ proactive/ salute/ charismatic/ meticulously/ unforgettable'],
                                  'negative': [
                                      'attack/ damage/ noise/ darkness/ worst/ shit/ fuck/ warned/ disappointed/ impose/ opponent/ restriction/ complain/ disagree/ siege/ hateful/ scandals/ bashing']},
                              19: {'positive': [
                                  'freedom/ protection/ gold/ spiritual/ liked/ relief/ magic/ skill/ pride/ grateful/ succeeded/ defeat/ gains/ advocate/ fantastic/ wins/ paradise/ proactive/ humorous'],
                                  'negative': [
                                      'negative/ attack/ broken/ damage/ noise/ darkness/ shit/ fuck/ rage/ impose/ nonsense/ opponent/ incomplete/ disagree/ poorer/ rogue/ sabotage/ insensitive/ breakup']},
                              20: {'positive': [
                                  'patient/ smile/ clearly/ freedom/ protection/ gold/ relief/ magic/ stronger/ skill/ pride/ defeat/ educated/ merry/ fiery/ brighter/ proactive/ salute/ personalized/ inspirational'],
                                  'negative': [
                                      'negative/ attack/ damage/ noise/ darkness/ limit/ shit/ fuck/ disappointed/ impose/ rape/ opponent/ rude/ complain/ siege/ rogue/ hateful/ insensitive/ scandals/ bashing']}}



        hypothesis_emo_synsand_LTOS = {2: {'positive': ['encouraging and redemption'], 'negative': ['worst and sneaky']},
                             3: {'positive': ['encouraging and constructive and proactive'],
                                 'negative': ['disappointed and needy and sneaky']},
                             4: {'positive': ['relief and encouraging and constructive and proactive'],
                                 'negative': ['attack and disappointed and needy and sneaky']},
                             5: {'positive': ['relief and pride and defeat and encouraging and constructive'],
                                 'negative': ['attack and unsure and naughty and divisive and sneaky']}, 6: {
        'positive': ['relief and pride and defeat and paradise and personalized and truthful'],
        'negative': ['attack and broken and damage and waning and divisive and sneaky']}, 7: {
        'positive': ['gold and relief and pride and defeat and paradise and personalized and truthful'],
        'negative': ['attack and damage and racism and fearful and lied and sneaky and bashing']}, 8: {
        'positive': [
            'gold and relief and pride and grateful and defeat and skilled and ecstatic and renaissance'],
        'negative': ['attack and damage and racism and impose and opponent and fearful and lied and bashing']},
                             9: {'positive': [
                                 'freedom and protection and gold and pride and grateful and defeat and skilled and ecstatic and renaissance'],
                                 'negative': [
                                     'attack and damage and rage and impose and opponent and complain and devastated and naughty and haunting']},
                             10: {'positive': [
                                 'clearly and freedom and protection and gold and pride and defeat and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and rage and disappointed and impose and opponent and complain and hateful and waning']},
                             11: {'positive': [
                                 'freedom and protection and gold and fun and pride and eager and defeat and constructive and elegance and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and rage and assault and disappointed and impose and opponent and complain and hateful and waning']},
                             12: {'positive': [
                                 'clearly and freedom and protection and gold and magic and skill and pride and defeat and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             13: {'positive': [
                                 'freedom and protection and gold and magic and skill and pride and defeat and intimate and gains and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and darkness and fuck and assault and disappointed and racism and impose and opponent and complain and falsehood and insensitive and waning']},
                             14: {'positive': [
                                 'smile and freedom and protection and popular and gold and magic and skill and pride and honor and defeat and educated and skilled and constructive and unforgettable'],
                                 'negative': [
                                     'negative and attack and damage and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             15: {'positive': [
                                 'smile and freedom and protection and popular and gold and magic and skill and pride and defeat and educated and skilled and constructive and proactive and vigilance and unforgettable'],
                                 'negative': [
                                     'negative and attack and damage and noise and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             16: {'positive': [
                                 'patient and smile and freedom and protection and popular and gold and magic and skill and pride and grateful and eager and defeat and delicate and proactive and salute and personalized'],
                                 'negative': [
                                     'negative and attack and damage and absence and darkness and worried and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and extremist']},
                             17: {'positive': [
                                 'freedom and protection and popular and gold and relief and magic and skill and pride and honor and defeat and gains and skilled and fantastic and constructive and tempting and proactive and unforgettable'],
                                 'negative': [
                                     'attack and broken and damage and noise and darkness and shit and fuck and assault and impose and opponent and bruised and hateful and insensitive and scandals and satirical and discouraging and bashing']},
                             18: {'positive': [
                                 'patient and clearly and freedom and protection and gold and relief and magic and skill and pride and defeat and educated and gains and skilled and proactive and salute and charismatic and meticulously and unforgettable'],
                                 'negative': [
                                     'attack and damage and noise and darkness and worst and shit and fuck and warned and disappointed and impose and opponent and restriction and complain and disagree and siege and hateful and scandals and bashing']},
                             19: {'positive': [
                                 'freedom and protection and gold and spiritual and liked and relief and magic and skill and pride and grateful and succeeded and defeat and gains and advocate and fantastic and wins and paradise and proactive and humorous'],
                                 'negative': [
                                     'negative and attack and broken and damage and noise and darkness and shit and fuck and rage and impose and nonsense and opponent and incomplete and disagree and poorer and rogue and sabotage and insensitive and breakup']},
                             20: {'positive': [
                                 'patient and smile and clearly and freedom and protection and gold and relief and magic and stronger and skill and pride and defeat and educated and merry and fiery and brighter and proactive and salute and personalized and inspirational'],
                                 'negative': [
                                     'negative and attack and damage and noise and darkness and limit and shit and fuck and disappointed and impose and rape and opponent and rude and complain and siege and rogue and hateful and insensitive and scandals and bashing']}}


    else:
        hypothesis_emo_syns_LTOS ={2: {'positive': ['encouraging, redemption'], 'negative': ['worst, sneaky']},
                                  3: {'positive': ['proactive, constructive, encouraging'],
                                      'negative': ['disappointed, needy, sneaky']},
                                  4: {'positive': ['proactive, constructive, relief, encouraging'],
                                      'negative': ['attack, disappointed, needy, sneaky']},
                                  5: {'positive': ['constructive, relief, encouraging, pride, defeat'],
                                      'negative': ['unsure, attack, divisive, naughty, sneaky']},
                                  6: {'positive': ['personalized, relief, pride, truthful, defeat, paradise'],
                                      'negative': ['damage, waning, broken, attack, divisive, sneaky']},
                                  7: {'positive': ['personalized, gold, relief, pride, truthful, defeat, paradise'],
                                      'negative': ['damage, bashing, attack, fearful, lied, sneaky, racism']}, 8: {
                'positive': ['skilled, renaissance, gold, ecstatic, grateful, relief, pride, defeat'],
                'negative': ['impose, damage, bashing, opponent, attack, fearful, lied, racism']}, 9: {
                'positive': ['skilled, renaissance, gold, ecstatic, grateful, protection, freedom, pride, defeat'],
                'negative': ['complain, impose, damage, opponent, attack, naughty, devastated, haunting, rage']}, 10: {
                'positive': [
                    'clearly, dazzling, personalized, vigilance, gold, ecstatic, protection, freedom, pride, defeat'],
                'negative': ['complain, impose, damage, waning, opponent, fuck, attack, disappointed, rage, hateful']},
                                  11: {'positive': [
                                      'eager, vigilance, constructive, elegance, gold, fun, ecstatic, protection, freedom, pride, defeat'],
                                       'negative': [
                                           'complain, impose, damage, waning, opponent, fuck, attack, disappointed, assault, rage, hateful']},
                                  12: {'positive': [
                                      'clearly, dazzling, personalized, vigilance, skill, gold, ecstatic, protection, freedom, pride, magic, defeat'],
                                       'negative': [
                                           'disagree, complain, impose, damage, bashing, opponent, fuck, attack, disappointed, scandals, satirical, haunting']},
                                  13: {'positive': [
                                      'gains, dazzling, personalized, vigilance, skill, gold, intimate, ecstatic, protection, freedom, pride, magic, defeat'],
                                       'negative': [
                                           'complain, impose, damage, waning, opponent, fuck, attack, disappointed, assault, falsehood, darkness, insensitive, racism']},
                                  14: {'positive': [
                                      'skilled, constructive, skill, unforgettable, educated, gold, smile, protection, freedom, honor, pride, magic, popular, defeat'],
                                       'negative': [
                                           'negative, disagree, complain, shit, impose, damage, bashing, opponent, fuck, attack, disappointed, scandals, satirical, haunting']},
                                  15: {'positive': [
                                      'proactive, skilled, vigilance, constructive, skill, unforgettable, educated, gold, smile, protection, freedom, pride, magic, popular, defeat'],
                                       'negative': [
                                           'negative, disagree, complain, shit, impose, damage, bashing, opponent, fuck, attack, disappointed, scandals, noise, satirical, haunting']},
                                  16: {'positive': [
                                      'proactive, personalized, eager, skill, salute, gold, smile, delicate, grateful, protection, patient, freedom, pride, magic, popular, defeat'],
                                       'negative': [
                                           'negative, disagree, complain, shit, impose, damage, opponent, fuck, worried, attack, disappointed, absence, scandals, extremist, haunting, darkness']},
                                  17: {'positive': [
                                      'fantastic, gains, proactive, skilled, constructive, skill, unforgettable, gold, protection, relief, freedom, honor, pride, tempting, magic, popular, defeat'],
                                       'negative': [
                                           'shit, impose, damage, bashing, opponent, broken, fuck, attack, bruised, assault, discouraging, scandals, noise, satirical, darkness, insensitive, hateful']},
                                  18: {'positive': [
                                      'clearly, gains, proactive, skilled, skill, charismatic, salute, meticulously, unforgettable, educated, gold, protection, patient, relief, freedom, pride, magic, defeat'],
                                       'negative': [
                                           'disagree, complain, shit, warned, impose, damage, restriction, siege, bashing, opponent, fuck, attack, disappointed, scandals, noise, worst, darkness, hateful']},
                                  19: {'positive': [
                                      'advocate, fantastic, gains, proactive, succeeded, wins, skill, liked, humorous, gold, grateful, protection, spiritual, relief, freedom, pride, magic, defeat, paradise'],
                                       'negative': [
                                           'negative, disagree, incomplete, shit, impose, damage, poorer, opponent, broken, fuck, attack, breakup, rogue, nonsense, noise, darkness, sabotage, insensitive, rage']},
                                  20: {'positive': [
                                      'clearly, proactive, personalized, stronger, skill, salute, educated, gold, brighter, smile, fiery, inspirational, merry, protection, patient, relief, freedom, pride, magic, defeat'],
                                       'negative': [
                                           'negative, limit, complain, shit, impose, damage, siege, bashing, opponent, fuck, attack, disappointed, rogue, scandals, noise, rude, darkness, insensitive, hateful, rape']}}


        hypothesis_emo_synspace_LTOS = {2: {'positive': ['encouraging redemption'], 'negative': ['worst sneaky']},
                                      3: {'positive': ['proactive constructive encouraging'],
                                          'negative': ['disappointed needy sneaky']},
                                      4: {'positive': ['proactive constructive relief encouraging'],
                                          'negative': ['attack disappointed needy sneaky']},
                                      5: {'positive': ['constructive relief encouraging pride defeat'],
                                          'negative': ['unsure attack divisive naughty sneaky']},
                                      6: {'positive': ['personalized relief pride truthful defeat paradise'],
                                          'negative': ['damage waning broken attack divisive sneaky']},
                                      7: {'positive': ['personalized gold relief pride truthful defeat paradise'],
                                          'negative': ['damage bashing attack fearful lied sneaky racism']}, 8: {
                'positive': ['skilled renaissance gold ecstatic grateful relief pride defeat'],
                'negative': ['impose damage bashing opponent attack fearful lied racism']}, 9: {
                'positive': ['skilled renaissance gold ecstatic grateful protection freedom pride defeat'],
                'negative': ['complain impose damage opponent attack naughty devastated haunting rage']}, 10: {
                'positive': ['clearly dazzling personalized vigilance gold ecstatic protection freedom pride defeat'],
                'negative': ['complain impose damage waning opponent fuck attack disappointed rage hateful']}, 11: {
                'positive': ['eager vigilance constructive elegance gold fun ecstatic protection freedom pride defeat'],
                'negative': ['complain impose damage waning opponent fuck attack disappointed assault rage hateful']},
                                      12: {'positive': [
                                          'clearly dazzling personalized vigilance skill gold ecstatic protection freedom pride magic defeat'],
                                           'negative': [
                                               'disagree complain impose damage bashing opponent fuck attack disappointed scandals satirical haunting']},
                                      13: {'positive': [
                                          'gains dazzling personalized vigilance skill gold intimate ecstatic protection freedom pride magic defeat'],
                                           'negative': [
                                               'complain impose damage waning opponent fuck attack disappointed assault falsehood darkness insensitive racism']},
                                      14: {'positive': [
                                          'skilled constructive skill unforgettable educated gold smile protection freedom honor pride magic popular defeat'],
                                           'negative': [
                                               'negative disagree complain shit impose damage bashing opponent fuck attack disappointed scandals satirical haunting']},
                                      15: {'positive': [
                                          'proactive skilled vigilance constructive skill unforgettable educated gold smile protection freedom pride magic popular defeat'],
                                           'negative': [
                                               'negative disagree complain shit impose damage bashing opponent fuck attack disappointed scandals noise satirical haunting']},
                                      16: {'positive': [
                                          'proactive personalized eager skill salute gold smile delicate grateful protection patient freedom pride magic popular defeat'],
                                           'negative': [
                                               'negative disagree complain shit impose damage opponent fuck worried attack disappointed absence scandals extremist haunting darkness']},
                                      17: {'positive': [
                                          'fantastic gains proactive skilled constructive skill unforgettable gold protection relief freedom honor pride tempting magic popular defeat'],
                                           'negative': [
                                               'shit impose damage bashing opponent broken fuck attack bruised assault discouraging scandals noise satirical darkness insensitive hateful']},
                                      18: {'positive': [
                                          'clearly gains proactive skilled skill charismatic salute meticulously unforgettable educated gold protection patient relief freedom pride magic defeat'],
                                           'negative': [
                                               'disagree complain shit warned impose damage restriction siege bashing opponent fuck attack disappointed scandals noise worst darkness hateful']},
                                      19: {'positive': [
                                          'advocate fantastic gains proactive succeeded wins skill liked humorous gold grateful protection spiritual relief freedom pride magic defeat paradise'],
                                           'negative': [
                                               'negative disagree incomplete shit impose damage poorer opponent broken fuck attack breakup rogue nonsense noise darkness sabotage insensitive rage']},
                                      20: {'positive': [
                                          'clearly proactive personalized stronger skill salute educated gold brighter smile fiery inspirational merry protection patient relief freedom pride magic defeat'],
                                           'negative': [
                                               'negative limit complain shit impose damage siege bashing opponent fuck attack disappointed rogue scandals noise rude darkness insensitive hateful rape']}}

        hypothesis_emo_synslash_LTOS = {2: {'positive': ['encouraging/ redemption'], 'negative': ['worst/ sneaky']},
                                      3: {'positive': ['proactive/ constructive/ encouraging'],
                                          'negative': ['disappointed/ needy/ sneaky']},
                                      4: {'positive': ['proactive/ constructive/ relief/ encouraging'],
                                          'negative': ['attack/ disappointed/ needy/ sneaky']},
                                      5: {'positive': ['constructive/ relief/ encouraging/ pride/ defeat'],
                                          'negative': ['unsure/ attack/ divisive/ naughty/ sneaky']},
                                      6: {'positive': ['personalized/ relief/ pride/ truthful/ defeat/ paradise'],
                                          'negative': ['damage/ waning/ broken/ attack/ divisive/ sneaky']},
                                      7: {'positive': ['personalized/ gold/ relief/ pride/ truthful/ defeat/ paradise'],
                                          'negative': ['damage/ bashing/ attack/ fearful/ lied/ sneaky/ racism']}, 8: {
                'positive': ['skilled/ renaissance/ gold/ ecstatic/ grateful/ relief/ pride/ defeat'],
                'negative': ['impose/ damage/ bashing/ opponent/ attack/ fearful/ lied/ racism']}, 9: {
                'positive': ['skilled/ renaissance/ gold/ ecstatic/ grateful/ protection/ freedom/ pride/ defeat'],
                'negative': ['complain/ impose/ damage/ opponent/ attack/ naughty/ devastated/ haunting/ rage']}, 10: {
                'positive': [
                    'clearly/ dazzling/ personalized/ vigilance/ gold/ ecstatic/ protection/ freedom/ pride/ defeat'],
                'negative': ['complain/ impose/ damage/ waning/ opponent/ fuck/ attack/ disappointed/ rage/ hateful']},
                                      11: {'positive': [
                                          'eager/ vigilance/ constructive/ elegance/ gold/ fun/ ecstatic/ protection/ freedom/ pride/ defeat'],
                                           'negative': [
                                               'complain/ impose/ damage/ waning/ opponent/ fuck/ attack/ disappointed/ assault/ rage/ hateful']},
                                      12: {'positive': [
                                          'clearly/ dazzling/ personalized/ vigilance/ skill/ gold/ ecstatic/ protection/ freedom/ pride/ magic/ defeat'],
                                           'negative': [
                                               'disagree/ complain/ impose/ damage/ bashing/ opponent/ fuck/ attack/ disappointed/ scandals/ satirical/ haunting']},
                                      13: {'positive': [
                                          'gains/ dazzling/ personalized/ vigilance/ skill/ gold/ intimate/ ecstatic/ protection/ freedom/ pride/ magic/ defeat'],
                                           'negative': [
                                               'complain/ impose/ damage/ waning/ opponent/ fuck/ attack/ disappointed/ assault/ falsehood/ darkness/ insensitive/ racism']},
                                      14: {'positive': [
                                          'skilled/ constructive/ skill/ unforgettable/ educated/ gold/ smile/ protection/ freedom/ honor/ pride/ magic/ popular/ defeat'],
                                           'negative': [
                                               'negative/ disagree/ complain/ shit/ impose/ damage/ bashing/ opponent/ fuck/ attack/ disappointed/ scandals/ satirical/ haunting']},
                                      15: {'positive': [
                                          'proactive/ skilled/ vigilance/ constructive/ skill/ unforgettable/ educated/ gold/ smile/ protection/ freedom/ pride/ magic/ popular/ defeat'],
                                           'negative': [
                                               'negative/ disagree/ complain/ shit/ impose/ damage/ bashing/ opponent/ fuck/ attack/ disappointed/ scandals/ noise/ satirical/ haunting']},
                                      16: {'positive': [
                                          'proactive/ personalized/ eager/ skill/ salute/ gold/ smile/ delicate/ grateful/ protection/ patient/ freedom/ pride/ magic/ popular/ defeat'],
                                           'negative': [
                                               'negative/ disagree/ complain/ shit/ impose/ damage/ opponent/ fuck/ worried/ attack/ disappointed/ absence/ scandals/ extremist/ haunting/ darkness']},
                                      17: {'positive': [
                                          'fantastic/ gains/ proactive/ skilled/ constructive/ skill/ unforgettable/ gold/ protection/ relief/ freedom/ honor/ pride/ tempting/ magic/ popular/ defeat'],
                                           'negative': [
                                               'shit/ impose/ damage/ bashing/ opponent/ broken/ fuck/ attack/ bruised/ assault/ discouraging/ scandals/ noise/ satirical/ darkness/ insensitive/ hateful']},
                                      18: {'positive': [
                                          'clearly/ gains/ proactive/ skilled/ skill/ charismatic/ salute/ meticulously/ unforgettable/ educated/ gold/ protection/ patient/ relief/ freedom/ pride/ magic/ defeat'],
                                           'negative': [
                                               'disagree/ complain/ shit/ warned/ impose/ damage/ restriction/ siege/ bashing/ opponent/ fuck/ attack/ disappointed/ scandals/ noise/ worst/ darkness/ hateful']},
                                      19: {'positive': [
                                          'advocate/ fantastic/ gains/ proactive/ succeeded/ wins/ skill/ liked/ humorous/ gold/ grateful/ protection/ spiritual/ relief/ freedom/ pride/ magic/ defeat/ paradise'],
                                           'negative': [
                                               'negative/ disagree/ incomplete/ shit/ impose/ damage/ poorer/ opponent/ broken/ fuck/ attack/ breakup/ rogue/ nonsense/ noise/ darkness/ sabotage/ insensitive/ rage']},
                                      20: {'positive': [
                                          'clearly/ proactive/ personalized/ stronger/ skill/ salute/ educated/ gold/ brighter/ smile/ fiery/ inspirational/ merry/ protection/ patient/ relief/ freedom/ pride/ magic/ defeat'],
                                           'negative': [
                                               'negative/ limit/ complain/ shit/ impose/ damage/ siege/ bashing/ opponent/ fuck/ attack/ disappointed/ rogue/ scandals/ noise/ rude/ darkness/ insensitive/ hateful/ rape']}}



        hypothesis_emo_synsand_LTOS = {2: {'positive': ['encouraging and redemption'], 'negative': ['worst and sneaky']},
                                     3: {'positive': ['proactive and constructive and encouraging'],
                                         'negative': ['disappointed and needy and sneaky']},
                                     4: {'positive': ['proactive and constructive and relief and encouraging'],
                                         'negative': ['attack and disappointed and needy and sneaky']},
                                     5: {'positive': ['constructive and relief and encouraging and pride and defeat'],
                                         'negative': ['unsure and attack and divisive and naughty and sneaky']}, 6: {
                'positive': ['personalized and relief and pride and truthful and defeat and paradise'],
                'negative': ['damage and waning and broken and attack and divisive and sneaky']}, 7: {
                'positive': ['personalized and gold and relief and pride and truthful and defeat and paradise'],
                'negative': ['damage and bashing and attack and fearful and lied and sneaky and racism']}, 8: {
                'positive': [
                    'skilled and renaissance and gold and ecstatic and grateful and relief and pride and defeat'],
                'negative': ['impose and damage and bashing and opponent and attack and fearful and lied and racism']},
                                     9: {'positive': [
                                         'skilled and renaissance and gold and ecstatic and grateful and protection and freedom and pride and defeat'],
                                         'negative': [
                                             'complain and impose and damage and opponent and attack and naughty and devastated and haunting and rage']},
                                     10: {'positive': [
                                         'clearly and dazzling and personalized and vigilance and gold and ecstatic and protection and freedom and pride and defeat'],
                                          'negative': [
                                              'complain and impose and damage and waning and opponent and fuck and attack and disappointed and rage and hateful']},
                                     11: {'positive': [
                                         'eager and vigilance and constructive and elegance and gold and fun and ecstatic and protection and freedom and pride and defeat'],
                                          'negative': [
                                              'complain and impose and damage and waning and opponent and fuck and attack and disappointed and assault and rage and hateful']},
                                     12: {'positive': [
                                         'clearly and dazzling and personalized and vigilance and skill and gold and ecstatic and protection and freedom and pride and magic and defeat'],
                                          'negative': [
                                              'disagree and complain and impose and damage and bashing and opponent and fuck and attack and disappointed and scandals and satirical and haunting']},
                                     13: {'positive': [
                                         'gains and dazzling and personalized and vigilance and skill and gold and intimate and ecstatic and protection and freedom and pride and magic and defeat'],
                                          'negative': [
                                              'complain and impose and damage and waning and opponent and fuck and attack and disappointed and assault and falsehood and darkness and insensitive and racism']},
                                     14: {'positive': [
                                         'skilled and constructive and skill and unforgettable and educated and gold and smile and protection and freedom and honor and pride and magic and popular and defeat'],
                                          'negative': [
                                              'negative and disagree and complain and shit and impose and damage and bashing and opponent and fuck and attack and disappointed and scandals and satirical and haunting']},
                                     15: {'positive': [
                                         'proactive and skilled and vigilance and constructive and skill and unforgettable and educated and gold and smile and protection and freedom and pride and magic and popular and defeat'],
                                          'negative': [
                                              'negative and disagree and complain and shit and impose and damage and bashing and opponent and fuck and attack and disappointed and scandals and noise and satirical and haunting']},
                                     16: {'positive': [
                                         'proactive and personalized and eager and skill and salute and gold and smile and delicate and grateful and protection and patient and freedom and pride and magic and popular and defeat'],
                                          'negative': [
                                              'negative and disagree and complain and shit and impose and damage and opponent and fuck and worried and attack and disappointed and absence and scandals and extremist and haunting and darkness']},
                                     17: {'positive': [
                                         'fantastic and gains and proactive and skilled and constructive and skill and unforgettable and gold and protection and relief and freedom and honor and pride and tempting and magic and popular and defeat'],
                                          'negative': [
                                              'shit and impose and damage and bashing and opponent and broken and fuck and attack and bruised and assault and discouraging and scandals and noise and satirical and darkness and insensitive and hateful']},
                                     18: {'positive': [
                                         'clearly and gains and proactive and skilled and skill and charismatic and salute and meticulously and unforgettable and educated and gold and protection and patient and relief and freedom and pride and magic and defeat'],
                                          'negative': [
                                              'disagree and complain and shit and warned and impose and damage and restriction and siege and bashing and opponent and fuck and attack and disappointed and scandals and noise and worst and darkness and hateful']},
                                     19: {'positive': [
                                         'advocate and fantastic and gains and proactive and succeeded and wins and skill and liked and humorous and gold and grateful and protection and spiritual and relief and freedom and pride and magic and defeat and paradise'],
                                          'negative': [
                                              'negative and disagree and incomplete and shit and impose and damage and poorer and opponent and broken and fuck and attack and breakup and rogue and nonsense and noise and darkness and sabotage and insensitive and rage']},
                                     20: {'positive': [
                                         'clearly and proactive and personalized and stronger and skill and salute and educated and gold and brighter and smile and fiery and inspirational and merry and protection and patient and relief and freedom and pride and magic and defeat'],
                                          'negative': [
                                              'negative and limit and complain and shit and impose and damage and siege and bashing and opponent and fuck and attack and disappointed and rogue and scandals and noise and rude and darkness and insensitive and hateful and rape']}}



    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 21)
    for dataname in datasetnames:
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = '32-shot-dataset/sa/' + dataname.upper() +'/'+ dataname.lower() + '_test.csv'
                        rows = []
                        with open(train) as f:
                            csv_read = csv.reader(f)
                            for row in csv_read:
                                label = ['positive', 'negative']
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

                            train =  '32-shot-dataset/sa/' + dataname.upper() +'/'+ dataname.lower() + '_test.csv'
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
                                            label = ['positive', 'negative']
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


def maincr(k):
    datasetnames = [
        'cr'
    ]
    traindev = [
        'train', 'dev',
        'test']
    if k == 'freq':
        hypothesis_emo_syns_LTOS =  {2: {'positive': ['encouraging, redemption'], 'negative': ['worst, sneaky']},
                          3: {'positive': ['encouraging, constructive, proactive'],
                              'negative': ['disappointed, needy, sneaky']},
                          4: {'positive': ['relief, encouraging, constructive, proactive'],
                              'negative': ['attack, disappointed, needy, sneaky']},
                          5: {'positive': ['relief, pride, defeat, encouraging, constructive'],
                              'negative': ['attack, unsure, naughty, divisive, sneaky']},
                          6: {'positive': ['relief, pride, defeat, paradise, personalized, truthful'],
                              'negative': ['attack, broken, damage, waning, divisive, sneaky']},
                          7: {'positive': ['gold, relief, pride, defeat, paradise, personalized, truthful'],
                              'negative': ['attack, damage, racism, fearful, lied, sneaky, bashing']}, 8: {
        'positive': ['gold, relief, pride, grateful, defeat, skilled, ecstatic, renaissance'],
        'negative': ['attack, damage, racism, impose, opponent, fearful, lied, bashing']}, 9: {
        'positive': ['freedom, protection, gold, pride, grateful, defeat, skilled, ecstatic, renaissance'],
        'negative': ['attack, damage, rage, impose, opponent, complain, devastated, naughty, haunting']}, 10: {
        'positive': [
            'clearly, freedom, protection, gold, pride, defeat, dazzling, personalized, vigilance, ecstatic'],
        'negative': ['attack, damage, fuck, rage, disappointed, impose, opponent, complain, hateful, waning']},
                          11: {'positive': [
                              'freedom, protection, gold, fun, pride, eager, defeat, constructive, elegance, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, fuck, rage, assault, disappointed, impose, opponent, complain, hateful, waning']},
                          12: {'positive': [
                              'clearly, freedom, protection, gold, magic, skill, pride, defeat, dazzling, personalized, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          13: {'positive': [
                              'freedom, protection, gold, magic, skill, pride, defeat, intimate, gains, dazzling, personalized, vigilance, ecstatic'],
                              'negative': [
                                  'attack, damage, darkness, fuck, assault, disappointed, racism, impose, opponent, complain, falsehood, insensitive, waning']},
                          14: {'positive': [
                              'smile, freedom, protection, popular, gold, magic, skill, pride, honor, defeat, educated, skilled, constructive, unforgettable'],
                              'negative': [
                                  'negative, attack, damage, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          15: {'positive': [
                              'smile, freedom, protection, popular, gold, magic, skill, pride, defeat, educated, skilled, constructive, proactive, vigilance, unforgettable'],
                              'negative': [
                                  'negative, attack, damage, noise, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, satirical, bashing']},
                          16: {'positive': [
                              'patient, smile, freedom, protection, popular, gold, magic, skill, pride, grateful, eager, defeat, delicate, proactive, salute, personalized'],
                              'negative': [
                                  'negative, attack, damage, absence, darkness, worried, shit, fuck, disappointed, impose, opponent, complain, disagree, haunting, scandals, extremist']},
                          17: {'positive': [
                              'freedom, protection, popular, gold, relief, magic, skill, pride, honor, defeat, gains, skilled, fantastic, constructive, tempting, proactive, unforgettable'],
                              'negative': [
                                  'attack, broken, damage, noise, darkness, shit, fuck, assault, impose, opponent, bruised, hateful, insensitive, scandals, satirical, discouraging, bashing']},
                          18: {'positive': [
                              'patient, clearly, freedom, protection, gold, relief, magic, skill, pride, defeat, educated, gains, skilled, proactive, salute, charismatic, meticulously, unforgettable'],
                              'negative': [
                                  'attack, damage, noise, darkness, worst, shit, fuck, warned, disappointed, impose, opponent, restriction, complain, disagree, siege, hateful, scandals, bashing']},
                          19: {'positive': [
                              'freedom, protection, gold, spiritual, liked, relief, magic, skill, pride, grateful, succeeded, defeat, gains, advocate, fantastic, wins, paradise, proactive, humorous'],
                              'negative': [
                                  'negative, attack, broken, damage, noise, darkness, shit, fuck, rage, impose, nonsense, opponent, incomplete, disagree, poorer, rogue, sabotage, insensitive, breakup']},
                          20: {'positive': [
                              'patient, smile, clearly, freedom, protection, gold, relief, magic, stronger, skill, pride, defeat, educated, merry, fiery, brighter, proactive, salute, personalized, inspirational'],
                              'negative': [
                                  'negative, attack, damage, noise, darkness, limit, shit, fuck, disappointed, impose, rape, opponent, rude, complain, siege, rogue, hateful, insensitive, scandals, bashing']}}



        hypothesis_emo_synspace_LTOS =  {2: {'positive': ['encouraging redemption'], 'negative': ['worst sneaky']},
                              3: {'positive': ['encouraging constructive proactive'],
                                  'negative': ['disappointed needy sneaky']},
                              4: {'positive': ['relief encouraging constructive proactive'],
                                  'negative': ['attack disappointed needy sneaky']},
                              5: {'positive': ['relief pride defeat encouraging constructive'],
                                  'negative': ['attack unsure naughty divisive sneaky']},
                              6: {'positive': ['relief pride defeat paradise personalized truthful'],
                                  'negative': ['attack broken damage waning divisive sneaky']},
                              7: {'positive': ['gold relief pride defeat paradise personalized truthful'],
                                  'negative': ['attack damage racism fearful lied sneaky bashing']}, 8: {
        'positive': ['gold relief pride grateful defeat skilled ecstatic renaissance'],
        'negative': ['attack damage racism impose opponent fearful lied bashing']}, 9: {
        'positive': ['freedom protection gold pride grateful defeat skilled ecstatic renaissance'],
        'negative': ['attack damage rage impose opponent complain devastated naughty haunting']}, 10: {
        'positive': ['clearly freedom protection gold pride defeat dazzling personalized vigilance ecstatic'],
        'negative': ['attack damage fuck rage disappointed impose opponent complain hateful waning']}, 11: {
        'positive': ['freedom protection gold fun pride eager defeat constructive elegance vigilance ecstatic'],
        'negative': ['attack damage fuck rage assault disappointed impose opponent complain hateful waning']},
                              12: {'positive': [
                                  'clearly freedom protection gold magic skill pride defeat dazzling personalized vigilance ecstatic'],
                                  'negative': [
                                      'attack damage fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              13: {'positive': [
                                  'freedom protection gold magic skill pride defeat intimate gains dazzling personalized vigilance ecstatic'],
                                  'negative': [
                                      'attack damage darkness fuck assault disappointed racism impose opponent complain falsehood insensitive waning']},
                              14: {'positive': [
                                  'smile freedom protection popular gold magic skill pride honor defeat educated skilled constructive unforgettable'],
                                  'negative': [
                                      'negative attack damage shit fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              15: {'positive': [
                                  'smile freedom protection popular gold magic skill pride defeat educated skilled constructive proactive vigilance unforgettable'],
                                  'negative': [
                                      'negative attack damage noise shit fuck disappointed impose opponent complain disagree haunting scandals satirical bashing']},
                              16: {'positive': [
                                  'patient smile freedom protection popular gold magic skill pride grateful eager defeat delicate proactive salute personalized'],
                                  'negative': [
                                      'negative attack damage absence darkness worried shit fuck disappointed impose opponent complain disagree haunting scandals extremist']},
                              17: {'positive': [
                                  'freedom protection popular gold relief magic skill pride honor defeat gains skilled fantastic constructive tempting proactive unforgettable'],
                                  'negative': [
                                      'attack broken damage noise darkness shit fuck assault impose opponent bruised hateful insensitive scandals satirical discouraging bashing']},
                              18: {'positive': [
                                  'patient clearly freedom protection gold relief magic skill pride defeat educated gains skilled proactive salute charismatic meticulously unforgettable'],
                                  'negative': [
                                      'attack damage noise darkness worst shit fuck warned disappointed impose opponent restriction complain disagree siege hateful scandals bashing']},
                              19: {'positive': [
                                  'freedom protection gold spiritual liked relief magic skill pride grateful succeeded defeat gains advocate fantastic wins paradise proactive humorous'],
                                  'negative': [
                                      'negative attack broken damage noise darkness shit fuck rage impose nonsense opponent incomplete disagree poorer rogue sabotage insensitive breakup']},
                              20: {'positive': [
                                  'patient smile clearly freedom protection gold relief magic stronger skill pride defeat educated merry fiery brighter proactive salute personalized inspirational'],
                                  'negative': [
                                      'negative attack damage noise darkness limit shit fuck disappointed impose rape opponent rude complain siege rogue hateful insensitive scandals bashing']}}



        hypothesis_emo_synslash_LTOS = {2: {'positive': ['encouraging/ redemption'], 'negative': ['worst/ sneaky']},
                              3: {'positive': ['encouraging/ constructive/ proactive'],
                                  'negative': ['disappointed/ needy/ sneaky']},
                              4: {'positive': ['relief/ encouraging/ constructive/ proactive'],
                                  'negative': ['attack/ disappointed/ needy/ sneaky']},
                              5: {'positive': ['relief/ pride/ defeat/ encouraging/ constructive'],
                                  'negative': ['attack/ unsure/ naughty/ divisive/ sneaky']},
                              6: {'positive': ['relief/ pride/ defeat/ paradise/ personalized/ truthful'],
                                  'negative': ['attack/ broken/ damage/ waning/ divisive/ sneaky']},
                              7: {'positive': ['gold/ relief/ pride/ defeat/ paradise/ personalized/ truthful'],
                                  'negative': ['attack/ damage/ racism/ fearful/ lied/ sneaky/ bashing']}, 8: {
        'positive': ['gold/ relief/ pride/ grateful/ defeat/ skilled/ ecstatic/ renaissance'],
        'negative': ['attack/ damage/ racism/ impose/ opponent/ fearful/ lied/ bashing']}, 9: {
        'positive': ['freedom/ protection/ gold/ pride/ grateful/ defeat/ skilled/ ecstatic/ renaissance'],
        'negative': ['attack/ damage/ rage/ impose/ opponent/ complain/ devastated/ naughty/ haunting']}, 10: {
        'positive': [
            'clearly/ freedom/ protection/ gold/ pride/ defeat/ dazzling/ personalized/ vigilance/ ecstatic'],
        'negative': ['attack/ damage/ fuck/ rage/ disappointed/ impose/ opponent/ complain/ hateful/ waning']},
                              11: {'positive': [
                                  'freedom/ protection/ gold/ fun/ pride/ eager/ defeat/ constructive/ elegance/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ fuck/ rage/ assault/ disappointed/ impose/ opponent/ complain/ hateful/ waning']},
                              12: {'positive': [
                                  'clearly/ freedom/ protection/ gold/ magic/ skill/ pride/ defeat/ dazzling/ personalized/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              13: {'positive': [
                                  'freedom/ protection/ gold/ magic/ skill/ pride/ defeat/ intimate/ gains/ dazzling/ personalized/ vigilance/ ecstatic'],
                                  'negative': [
                                      'attack/ damage/ darkness/ fuck/ assault/ disappointed/ racism/ impose/ opponent/ complain/ falsehood/ insensitive/ waning']},
                              14: {'positive': [
                                  'smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ honor/ defeat/ educated/ skilled/ constructive/ unforgettable'],
                                  'negative': [
                                      'negative/ attack/ damage/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              15: {'positive': [
                                  'smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ defeat/ educated/ skilled/ constructive/ proactive/ vigilance/ unforgettable'],
                                  'negative': [
                                      'negative/ attack/ damage/ noise/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ satirical/ bashing']},
                              16: {'positive': [
                                  'patient/ smile/ freedom/ protection/ popular/ gold/ magic/ skill/ pride/ grateful/ eager/ defeat/ delicate/ proactive/ salute/ personalized'],
                                  'negative': [
                                      'negative/ attack/ damage/ absence/ darkness/ worried/ shit/ fuck/ disappointed/ impose/ opponent/ complain/ disagree/ haunting/ scandals/ extremist']},
                              17: {'positive': [
                                  'freedom/ protection/ popular/ gold/ relief/ magic/ skill/ pride/ honor/ defeat/ gains/ skilled/ fantastic/ constructive/ tempting/ proactive/ unforgettable'],
                                  'negative': [
                                      'attack/ broken/ damage/ noise/ darkness/ shit/ fuck/ assault/ impose/ opponent/ bruised/ hateful/ insensitive/ scandals/ satirical/ discouraging/ bashing']},
                              18: {'positive': [
                                  'patient/ clearly/ freedom/ protection/ gold/ relief/ magic/ skill/ pride/ defeat/ educated/ gains/ skilled/ proactive/ salute/ charismatic/ meticulously/ unforgettable'],
                                  'negative': [
                                      'attack/ damage/ noise/ darkness/ worst/ shit/ fuck/ warned/ disappointed/ impose/ opponent/ restriction/ complain/ disagree/ siege/ hateful/ scandals/ bashing']},
                              19: {'positive': [
                                  'freedom/ protection/ gold/ spiritual/ liked/ relief/ magic/ skill/ pride/ grateful/ succeeded/ defeat/ gains/ advocate/ fantastic/ wins/ paradise/ proactive/ humorous'],
                                  'negative': [
                                      'negative/ attack/ broken/ damage/ noise/ darkness/ shit/ fuck/ rage/ impose/ nonsense/ opponent/ incomplete/ disagree/ poorer/ rogue/ sabotage/ insensitive/ breakup']},
                              20: {'positive': [
                                  'patient/ smile/ clearly/ freedom/ protection/ gold/ relief/ magic/ stronger/ skill/ pride/ defeat/ educated/ merry/ fiery/ brighter/ proactive/ salute/ personalized/ inspirational'],
                                  'negative': [
                                      'negative/ attack/ damage/ noise/ darkness/ limit/ shit/ fuck/ disappointed/ impose/ rape/ opponent/ rude/ complain/ siege/ rogue/ hateful/ insensitive/ scandals/ bashing']}}



        hypothesis_emo_synsand_LTOS = {2: {'positive': ['encouraging and redemption'], 'negative': ['worst and sneaky']},
                             3: {'positive': ['encouraging and constructive and proactive'],
                                 'negative': ['disappointed and needy and sneaky']},
                             4: {'positive': ['relief and encouraging and constructive and proactive'],
                                 'negative': ['attack and disappointed and needy and sneaky']},
                             5: {'positive': ['relief and pride and defeat and encouraging and constructive'],
                                 'negative': ['attack and unsure and naughty and divisive and sneaky']}, 6: {
        'positive': ['relief and pride and defeat and paradise and personalized and truthful'],
        'negative': ['attack and broken and damage and waning and divisive and sneaky']}, 7: {
        'positive': ['gold and relief and pride and defeat and paradise and personalized and truthful'],
        'negative': ['attack and damage and racism and fearful and lied and sneaky and bashing']}, 8: {
        'positive': [
            'gold and relief and pride and grateful and defeat and skilled and ecstatic and renaissance'],
        'negative': ['attack and damage and racism and impose and opponent and fearful and lied and bashing']},
                             9: {'positive': [
                                 'freedom and protection and gold and pride and grateful and defeat and skilled and ecstatic and renaissance'],
                                 'negative': [
                                     'attack and damage and rage and impose and opponent and complain and devastated and naughty and haunting']},
                             10: {'positive': [
                                 'clearly and freedom and protection and gold and pride and defeat and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and rage and disappointed and impose and opponent and complain and hateful and waning']},
                             11: {'positive': [
                                 'freedom and protection and gold and fun and pride and eager and defeat and constructive and elegance and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and rage and assault and disappointed and impose and opponent and complain and hateful and waning']},
                             12: {'positive': [
                                 'clearly and freedom and protection and gold and magic and skill and pride and defeat and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             13: {'positive': [
                                 'freedom and protection and gold and magic and skill and pride and defeat and intimate and gains and dazzling and personalized and vigilance and ecstatic'],
                                 'negative': [
                                     'attack and damage and darkness and fuck and assault and disappointed and racism and impose and opponent and complain and falsehood and insensitive and waning']},
                             14: {'positive': [
                                 'smile and freedom and protection and popular and gold and magic and skill and pride and honor and defeat and educated and skilled and constructive and unforgettable'],
                                 'negative': [
                                     'negative and attack and damage and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             15: {'positive': [
                                 'smile and freedom and protection and popular and gold and magic and skill and pride and defeat and educated and skilled and constructive and proactive and vigilance and unforgettable'],
                                 'negative': [
                                     'negative and attack and damage and noise and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and satirical and bashing']},
                             16: {'positive': [
                                 'patient and smile and freedom and protection and popular and gold and magic and skill and pride and grateful and eager and defeat and delicate and proactive and salute and personalized'],
                                 'negative': [
                                     'negative and attack and damage and absence and darkness and worried and shit and fuck and disappointed and impose and opponent and complain and disagree and haunting and scandals and extremist']},
                             17: {'positive': [
                                 'freedom and protection and popular and gold and relief and magic and skill and pride and honor and defeat and gains and skilled and fantastic and constructive and tempting and proactive and unforgettable'],
                                 'negative': [
                                     'attack and broken and damage and noise and darkness and shit and fuck and assault and impose and opponent and bruised and hateful and insensitive and scandals and satirical and discouraging and bashing']},
                             18: {'positive': [
                                 'patient and clearly and freedom and protection and gold and relief and magic and skill and pride and defeat and educated and gains and skilled and proactive and salute and charismatic and meticulously and unforgettable'],
                                 'negative': [
                                     'attack and damage and noise and darkness and worst and shit and fuck and warned and disappointed and impose and opponent and restriction and complain and disagree and siege and hateful and scandals and bashing']},
                             19: {'positive': [
                                 'freedom and protection and gold and spiritual and liked and relief and magic and skill and pride and grateful and succeeded and defeat and gains and advocate and fantastic and wins and paradise and proactive and humorous'],
                                 'negative': [
                                     'negative and attack and broken and damage and noise and darkness and shit and fuck and rage and impose and nonsense and opponent and incomplete and disagree and poorer and rogue and sabotage and insensitive and breakup']},
                             20: {'positive': [
                                 'patient and smile and clearly and freedom and protection and gold and relief and magic and stronger and skill and pride and defeat and educated and merry and fiery and brighter and proactive and salute and personalized and inspirational'],
                                 'negative': [
                                     'negative and attack and damage and noise and darkness and limit and shit and fuck and disappointed and impose and rape and opponent and rude and complain and siege and rogue and hateful and insensitive and scandals and bashing']}}


    else:
        hypothesis_emo_syns_LTOS ={2: {'positive': ['redemption, encouraging'], 'negative': ['worst, sneaky']},
                                  3: {'positive': ['constructive, proactive, encouraging'],
                                      'negative': ['disappointed, needy, sneaky']},
                                  4: {'positive': ['constructive, proactive, encouraging, relief'],
                                      'negative': ['disappointed, attack, needy, sneaky']},
                                  5: {'positive': ['constructive, encouraging, relief, pride, defeat'],
                                      'negative': ['unsure, attack, divisive, naughty, sneaky']},
                                  6: {'positive': ['truthful, personalized, relief, pride, paradise, defeat'],
                                      'negative': ['damage, broken, waning, attack, divisive, sneaky']},
                                  7: {'positive': ['truthful, personalized, gold, relief, pride, paradise, defeat'],
                                      'negative': ['bashing, damage, attack, fearful, lied, sneaky, racism']}, 8: {
                'positive': ['skilled, renaissance, grateful, ecstatic, gold, relief, pride, defeat'],
                'negative': ['impose, bashing, opponent, damage, attack, fearful, lied, racism']}, 9: {
                'positive': ['skilled, renaissance, grateful, protection, freedom, ecstatic, gold, pride, defeat'],
                'negative': ['complain, impose, opponent, damage, attack, naughty, rage, devastated, haunting']}, 10: {
                'positive': [
                    'clearly, vigilance, dazzling, protection, personalized, freedom, ecstatic, gold, pride, defeat'],
                'negative': ['complain, impose, opponent, damage, fuck, disappointed, waning, attack, rage, hateful']},
                                  11: {'positive': [
                                      'constructive, vigilance, eager, elegance, protection, freedom, ecstatic, gold, pride, fun, defeat'],
                                       'negative': [
                                           'complain, impose, opponent, damage, fuck, disappointed, waning, attack, assault, rage, hateful']},
                                  12: {'positive': [
                                      'clearly, vigilance, dazzling, skill, protection, personalized, freedom, ecstatic, gold, pride, magic, defeat'],
                                       'negative': [
                                           'complain, disagree, impose, bashing, opponent, damage, fuck, disappointed, scandals, attack, haunting, satirical']},
                                  13: {'positive': [
                                      'gains, vigilance, dazzling, skill, protection, personalized, freedom, ecstatic, gold, intimate, pride, magic, defeat'],
                                       'negative': [
                                           'complain, impose, opponent, damage, fuck, disappointed, waning, attack, assault, falsehood, darkness, insensitive, racism']},
                                  14: {'positive': [
                                      'constructive, skilled, educated, smile, skill, honor, protection, freedom, gold, pride, unforgettable, magic, popular, defeat'],
                                       'negative': [
                                           'negative, complain, disagree, impose, shit, bashing, opponent, damage, fuck, disappointed, scandals, attack, haunting, satirical']},
                                  15: {'positive': [
                                      'constructive, proactive, vigilance, skilled, educated, smile, skill, protection, freedom, gold, pride, unforgettable, magic, popular, defeat'],
                                       'negative': [
                                           'negative, complain, disagree, impose, shit, bashing, opponent, damage, fuck, disappointed, scandals, attack, noise, haunting, satirical']},
                                  16: {'positive': [
                                      'proactive, eager, salute, smile, skill, grateful, protection, personalized, freedom, gold, pride, patient, magic, delicate, popular, defeat'],
                                       'negative': [
                                           'negative, complain, disagree, impose, shit, worried, opponent, damage, absence, fuck, disappointed, scandals, attack, extremist, darkness, haunting']},
                                  17: {'positive': [
                                      'gains, constructive, fantastic, proactive, skilled, skill, honor, protection, freedom, gold, relief, pride, unforgettable, magic, tempting, popular, defeat'],
                                       'negative': [
                                           'impose, shit, bashing, opponent, damage, fuck, broken, scandals, attack, assault, noise, bruised, discouraging, darkness, insensitive, satirical, hateful']},
                                  18: {'positive': [
                                      'clearly, gains, proactive, skilled, salute, educated, skill, meticulously, charismatic, protection, freedom, gold, relief, pride, patient, unforgettable, magic, defeat'],
                                       'negative': [
                                           'complain, disagree, restriction, warned, impose, siege, shit, bashing, opponent, damage, fuck, disappointed, scandals, attack, noise, worst, darkness, hateful']},
                                  19: {'positive': [
                                      'succeeded, gains, wins, fantastic, advocate, proactive, liked, skill, grateful, protection, freedom, gold, relief, pride, paradise, magic, spiritual, humorous, defeat'],
                                       'negative': [
                                           'negative, disagree, incomplete, impose, shit, poorer, opponent, breakup, damage, fuck, broken, attack, noise, rogue, rage, nonsense, darkness, insensitive, sabotage']},
                                  20: {'positive': [
                                      'clearly, proactive, salute, stronger, educated, smile, skill, merry, protection, personalized, freedom, gold, brighter, relief, pride, fiery, patient, magic, inspirational, defeat'],
                                       'negative': [
                                           'negative, complain, limit, impose, siege, shit, bashing, opponent, damage, fuck, disappointed, scandals, attack, noise, rogue, darkness, rape, insensitive, rude, hateful']}}


        hypothesis_emo_synspace_LTOS = {2: {'positive': ['redemption encouraging'], 'negative': ['worst sneaky']},
                                      3: {'positive': ['constructive proactive encouraging'],
                                          'negative': ['disappointed needy sneaky']},
                                      4: {'positive': ['constructive proactive encouraging relief'],
                                          'negative': ['disappointed attack needy sneaky']},
                                      5: {'positive': ['constructive encouraging relief pride defeat'],
                                          'negative': ['unsure attack divisive naughty sneaky']},
                                      6: {'positive': ['truthful personalized relief pride paradise defeat'],
                                          'negative': ['damage broken waning attack divisive sneaky']},
                                      7: {'positive': ['truthful personalized gold relief pride paradise defeat'],
                                          'negative': ['bashing damage attack fearful lied sneaky racism']}, 8: {
                'positive': ['skilled renaissance grateful ecstatic gold relief pride defeat'],
                'negative': ['impose bashing opponent damage attack fearful lied racism']}, 9: {
                'positive': ['skilled renaissance grateful protection freedom ecstatic gold pride defeat'],
                'negative': ['complain impose opponent damage attack naughty rage devastated haunting']}, 10: {
                'positive': ['clearly vigilance dazzling protection personalized freedom ecstatic gold pride defeat'],
                'negative': ['complain impose opponent damage fuck disappointed waning attack rage hateful']}, 11: {
                'positive': ['constructive vigilance eager elegance protection freedom ecstatic gold pride fun defeat'],
                'negative': ['complain impose opponent damage fuck disappointed waning attack assault rage hateful']},
                                      12: {'positive': [
                                          'clearly vigilance dazzling skill protection personalized freedom ecstatic gold pride magic defeat'],
                                           'negative': [
                                               'complain disagree impose bashing opponent damage fuck disappointed scandals attack haunting satirical']},
                                      13: {'positive': [
                                          'gains vigilance dazzling skill protection personalized freedom ecstatic gold intimate pride magic defeat'],
                                           'negative': [
                                               'complain impose opponent damage fuck disappointed waning attack assault falsehood darkness insensitive racism']},
                                      14: {'positive': [
                                          'constructive skilled educated smile skill honor protection freedom gold pride unforgettable magic popular defeat'],
                                           'negative': [
                                               'negative complain disagree impose shit bashing opponent damage fuck disappointed scandals attack haunting satirical']},
                                      15: {'positive': [
                                          'constructive proactive vigilance skilled educated smile skill protection freedom gold pride unforgettable magic popular defeat'],
                                           'negative': [
                                               'negative complain disagree impose shit bashing opponent damage fuck disappointed scandals attack noise haunting satirical']},
                                      16: {'positive': [
                                          'proactive eager salute smile skill grateful protection personalized freedom gold pride patient magic delicate popular defeat'],
                                           'negative': [
                                               'negative complain disagree impose shit worried opponent damage absence fuck disappointed scandals attack extremist darkness haunting']},
                                      17: {'positive': [
                                          'gains constructive fantastic proactive skilled skill honor protection freedom gold relief pride unforgettable magic tempting popular defeat'],
                                           'negative': [
                                               'impose shit bashing opponent damage fuck broken scandals attack assault noise bruised discouraging darkness insensitive satirical hateful']},
                                      18: {'positive': [
                                          'clearly gains proactive skilled salute educated skill meticulously charismatic protection freedom gold relief pride patient unforgettable magic defeat'],
                                           'negative': [
                                               'complain disagree restriction warned impose siege shit bashing opponent damage fuck disappointed scandals attack noise worst darkness hateful']},
                                      19: {'positive': [
                                          'succeeded gains wins fantastic advocate proactive liked skill grateful protection freedom gold relief pride paradise magic spiritual humorous defeat'],
                                           'negative': [
                                               'negative disagree incomplete impose shit poorer opponent breakup damage fuck broken attack noise rogue rage nonsense darkness insensitive sabotage']},
                                      20: {'positive': [
                                          'clearly proactive salute stronger educated smile skill merry protection personalized freedom gold brighter relief pride fiery patient magic inspirational defeat'],
                                           'negative': [
                                               'negative complain limit impose siege shit bashing opponent damage fuck disappointed scandals attack noise rogue darkness rape insensitive rude hateful']}}

        hypothesis_emo_synslash_LTOS ={2: {'positive': ['redemption/ encouraging'], 'negative': ['worst/ sneaky']},
                                      3: {'positive': ['constructive/ proactive/ encouraging'],
                                          'negative': ['disappointed/ needy/ sneaky']},
                                      4: {'positive': ['constructive/ proactive/ encouraging/ relief'],
                                          'negative': ['disappointed/ attack/ needy/ sneaky']},
                                      5: {'positive': ['constructive/ encouraging/ relief/ pride/ defeat'],
                                          'negative': ['unsure/ attack/ divisive/ naughty/ sneaky']},
                                      6: {'positive': ['truthful/ personalized/ relief/ pride/ paradise/ defeat'],
                                          'negative': ['damage/ broken/ waning/ attack/ divisive/ sneaky']},
                                      7: {'positive': ['truthful/ personalized/ gold/ relief/ pride/ paradise/ defeat'],
                                          'negative': ['bashing/ damage/ attack/ fearful/ lied/ sneaky/ racism']}, 8: {
                'positive': ['skilled/ renaissance/ grateful/ ecstatic/ gold/ relief/ pride/ defeat'],
                'negative': ['impose/ bashing/ opponent/ damage/ attack/ fearful/ lied/ racism']}, 9: {
                'positive': ['skilled/ renaissance/ grateful/ protection/ freedom/ ecstatic/ gold/ pride/ defeat'],
                'negative': ['complain/ impose/ opponent/ damage/ attack/ naughty/ rage/ devastated/ haunting']}, 10: {
                'positive': [
                    'clearly/ vigilance/ dazzling/ protection/ personalized/ freedom/ ecstatic/ gold/ pride/ defeat'],
                'negative': ['complain/ impose/ opponent/ damage/ fuck/ disappointed/ waning/ attack/ rage/ hateful']},
                                      11: {'positive': [
                                          'constructive/ vigilance/ eager/ elegance/ protection/ freedom/ ecstatic/ gold/ pride/ fun/ defeat'],
                                           'negative': [
                                               'complain/ impose/ opponent/ damage/ fuck/ disappointed/ waning/ attack/ assault/ rage/ hateful']},
                                      12: {'positive': [
                                          'clearly/ vigilance/ dazzling/ skill/ protection/ personalized/ freedom/ ecstatic/ gold/ pride/ magic/ defeat'],
                                           'negative': [
                                               'complain/ disagree/ impose/ bashing/ opponent/ damage/ fuck/ disappointed/ scandals/ attack/ haunting/ satirical']},
                                      13: {'positive': [
                                          'gains/ vigilance/ dazzling/ skill/ protection/ personalized/ freedom/ ecstatic/ gold/ intimate/ pride/ magic/ defeat'],
                                           'negative': [
                                               'complain/ impose/ opponent/ damage/ fuck/ disappointed/ waning/ attack/ assault/ falsehood/ darkness/ insensitive/ racism']},
                                      14: {'positive': [
                                          'constructive/ skilled/ educated/ smile/ skill/ honor/ protection/ freedom/ gold/ pride/ unforgettable/ magic/ popular/ defeat'],
                                           'negative': [
                                               'negative/ complain/ disagree/ impose/ shit/ bashing/ opponent/ damage/ fuck/ disappointed/ scandals/ attack/ haunting/ satirical']},
                                      15: {'positive': [
                                          'constructive/ proactive/ vigilance/ skilled/ educated/ smile/ skill/ protection/ freedom/ gold/ pride/ unforgettable/ magic/ popular/ defeat'],
                                           'negative': [
                                               'negative/ complain/ disagree/ impose/ shit/ bashing/ opponent/ damage/ fuck/ disappointed/ scandals/ attack/ noise/ haunting/ satirical']},
                                      16: {'positive': [
                                          'proactive/ eager/ salute/ smile/ skill/ grateful/ protection/ personalized/ freedom/ gold/ pride/ patient/ magic/ delicate/ popular/ defeat'],
                                           'negative': [
                                               'negative/ complain/ disagree/ impose/ shit/ worried/ opponent/ damage/ absence/ fuck/ disappointed/ scandals/ attack/ extremist/ darkness/ haunting']},
                                      17: {'positive': [
                                          'gains/ constructive/ fantastic/ proactive/ skilled/ skill/ honor/ protection/ freedom/ gold/ relief/ pride/ unforgettable/ magic/ tempting/ popular/ defeat'],
                                           'negative': [
                                               'impose/ shit/ bashing/ opponent/ damage/ fuck/ broken/ scandals/ attack/ assault/ noise/ bruised/ discouraging/ darkness/ insensitive/ satirical/ hateful']},
                                      18: {'positive': [
                                          'clearly/ gains/ proactive/ skilled/ salute/ educated/ skill/ meticulously/ charismatic/ protection/ freedom/ gold/ relief/ pride/ patient/ unforgettable/ magic/ defeat'],
                                           'negative': [
                                               'complain/ disagree/ restriction/ warned/ impose/ siege/ shit/ bashing/ opponent/ damage/ fuck/ disappointed/ scandals/ attack/ noise/ worst/ darkness/ hateful']},
                                      19: {'positive': [
                                          'succeeded/ gains/ wins/ fantastic/ advocate/ proactive/ liked/ skill/ grateful/ protection/ freedom/ gold/ relief/ pride/ paradise/ magic/ spiritual/ humorous/ defeat'],
                                           'negative': [
                                               'negative/ disagree/ incomplete/ impose/ shit/ poorer/ opponent/ breakup/ damage/ fuck/ broken/ attack/ noise/ rogue/ rage/ nonsense/ darkness/ insensitive/ sabotage']},
                                      20: {'positive': [
                                          'clearly/ proactive/ salute/ stronger/ educated/ smile/ skill/ merry/ protection/ personalized/ freedom/ gold/ brighter/ relief/ pride/ fiery/ patient/ magic/ inspirational/ defeat'],
                                           'negative': [
                                               'negative/ complain/ limit/ impose/ siege/ shit/ bashing/ opponent/ damage/ fuck/ disappointed/ scandals/ attack/ noise/ rogue/ darkness/ rape/ insensitive/ rude/ hateful']}}



        hypothesis_emo_synsand_LTOS ={2: {'positive': ['redemption and encouraging'], 'negative': ['worst and sneaky']},
                                     3: {'positive': ['constructive and proactive and encouraging'],
                                         'negative': ['disappointed and needy and sneaky']},
                                     4: {'positive': ['constructive and proactive and encouraging and relief'],
                                         'negative': ['disappointed and attack and needy and sneaky']},
                                     5: {'positive': ['constructive and encouraging and relief and pride and defeat'],
                                         'negative': ['unsure and attack and divisive and naughty and sneaky']}, 6: {
                'positive': ['truthful and personalized and relief and pride and paradise and defeat'],
                'negative': ['damage and broken and waning and attack and divisive and sneaky']}, 7: {
                'positive': ['truthful and personalized and gold and relief and pride and paradise and defeat'],
                'negative': ['bashing and damage and attack and fearful and lied and sneaky and racism']}, 8: {
                'positive': [
                    'skilled and renaissance and grateful and ecstatic and gold and relief and pride and defeat'],
                'negative': ['impose and bashing and opponent and damage and attack and fearful and lied and racism']},
                                     9: {'positive': [
                                         'skilled and renaissance and grateful and protection and freedom and ecstatic and gold and pride and defeat'],
                                         'negative': [
                                             'complain and impose and opponent and damage and attack and naughty and rage and devastated and haunting']},
                                     10: {'positive': [
                                         'clearly and vigilance and dazzling and protection and personalized and freedom and ecstatic and gold and pride and defeat'],
                                          'negative': [
                                              'complain and impose and opponent and damage and fuck and disappointed and waning and attack and rage and hateful']},
                                     11: {'positive': [
                                         'constructive and vigilance and eager and elegance and protection and freedom and ecstatic and gold and pride and fun and defeat'],
                                          'negative': [
                                              'complain and impose and opponent and damage and fuck and disappointed and waning and attack and assault and rage and hateful']},
                                     12: {'positive': [
                                         'clearly and vigilance and dazzling and skill and protection and personalized and freedom and ecstatic and gold and pride and magic and defeat'],
                                          'negative': [
                                              'complain and disagree and impose and bashing and opponent and damage and fuck and disappointed and scandals and attack and haunting and satirical']},
                                     13: {'positive': [
                                         'gains and vigilance and dazzling and skill and protection and personalized and freedom and ecstatic and gold and intimate and pride and magic and defeat'],
                                          'negative': [
                                              'complain and impose and opponent and damage and fuck and disappointed and waning and attack and assault and falsehood and darkness and insensitive and racism']},
                                     14: {'positive': [
                                         'constructive and skilled and educated and smile and skill and honor and protection and freedom and gold and pride and unforgettable and magic and popular and defeat'],
                                          'negative': [
                                              'negative and complain and disagree and impose and shit and bashing and opponent and damage and fuck and disappointed and scandals and attack and haunting and satirical']},
                                     15: {'positive': [
                                         'constructive and proactive and vigilance and skilled and educated and smile and skill and protection and freedom and gold and pride and unforgettable and magic and popular and defeat'],
                                          'negative': [
                                              'negative and complain and disagree and impose and shit and bashing and opponent and damage and fuck and disappointed and scandals and attack and noise and haunting and satirical']},
                                     16: {'positive': [
                                         'proactive and eager and salute and smile and skill and grateful and protection and personalized and freedom and gold and pride and patient and magic and delicate and popular and defeat'],
                                          'negative': [
                                              'negative and complain and disagree and impose and shit and worried and opponent and damage and absence and fuck and disappointed and scandals and attack and extremist and darkness and haunting']},
                                     17: {'positive': [
                                         'gains and constructive and fantastic and proactive and skilled and skill and honor and protection and freedom and gold and relief and pride and unforgettable and magic and tempting and popular and defeat'],
                                          'negative': [
                                              'impose and shit and bashing and opponent and damage and fuck and broken and scandals and attack and assault and noise and bruised and discouraging and darkness and insensitive and satirical and hateful']},
                                     18: {'positive': [
                                         'clearly and gains and proactive and skilled and salute and educated and skill and meticulously and charismatic and protection and freedom and gold and relief and pride and patient and unforgettable and magic and defeat'],
                                          'negative': [
                                              'complain and disagree and restriction and warned and impose and siege and shit and bashing and opponent and damage and fuck and disappointed and scandals and attack and noise and worst and darkness and hateful']},
                                     19: {'positive': [
                                         'succeeded and gains and wins and fantastic and advocate and proactive and liked and skill and grateful and protection and freedom and gold and relief and pride and paradise and magic and spiritual and humorous and defeat'],
                                          'negative': [
                                              'negative and disagree and incomplete and impose and shit and poorer and opponent and breakup and damage and fuck and broken and attack and noise and rogue and rage and nonsense and darkness and insensitive and sabotage']},
                                     20: {'positive': [
                                         'clearly and proactive and salute and stronger and educated and smile and skill and merry and protection and personalized and freedom and gold and brighter and relief and pride and fiery and patient and magic and inspirational and defeat'],
                                          'negative': [
                                              'negative and complain and limit and impose and siege and shit and bashing and opponent and damage and fuck and disappointed and scandals and attack and noise and rogue and darkness and rape and insensitive and rude and hateful']}}


    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 21)
    for dataname in datasetnames:
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = '32-shot-dataset/sa/' + dataname.upper() +'/'+ dataname.lower() + '_test.csv'
                        rows = []
                        with open(train) as f:
                            csv_read = csv.reader(f)
                            for row in csv_read:
                                label = ['positive', 'negative']
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
                            train = '32-shot-dataset/sa/CR/' + dataname.lower() + '_select_' + td + '_' + str(n) + '.csv'

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
                                            label = ['positive', 'negative']
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

def mainagnews(k):
    datasetnames = [
        'agnews'
    ]
    traindev = [
        'train', 'dev',
        'test']
    if k == 'freq':
        hypothesis_emo_syns_LTOS = {2: {'World': ['profit, expert'], 'Sports': ['football, bob'], 'Business': ['capital, prehistoric'], 'Tech': ['enterprise, developer']}, 3: {'World': ['education, officer, federal'], 'Sports': ['football, wage, competitions'], 'Business': ['capital, communications, transportation'], 'Tech': ['gold, computers, developer']}, 4: {'World': ['education, officer, federal, anarchism'], 'Sports': ['average, defense, wage, competitions'], 'Business': ['capital, stock, communications, transportation'], 'Tech': ['gold, psychology, enterprise, robotics']}, 5: {'World': ['education, tribute, bloc, minimalist, anarchism'], 'Sports': ['model, average, competition, defense, recreational'], 'Business': ['money, economic, capital, store, stock'], 'Tech': ['gold, skill, psychology, enterprise, biomedical']}, 6: {'World': ['education, property, tribute, bloc, minimalist, anarchism'], 'Sports': ['fun, defense, sports, football, golf, puck'], 'Business': ['money, resources, capital, stock, consumer, communications'], 'Tech': ['gold, solutions, skill, productivity, specialized, developer']}, 7: {'World': ['property, negotiation, tribute, allegiance, bloc, curfew, anarchism'], 'Sports': ['competition, defense, television, defence, tournament, wrestling, puck'], 'Business': ['money, economic, capital, stock, consumer, agriculture, communications'], 'Tech': ['value, gold, solutions, skill, psychology, specialized, developer']}, 8: {'World': ['education, property, ethics, petition, manipulation, tribute, imperialism, anarchism'], 'Sports': ['season, defense, defence, golf, soccer, tournament, wrestling, puck'], 'Business': ['money, resources, capital, stock, consumer, communications, commission, broker'], 'Tech': ['value, communication, gold, skill, specialized, technician, primates, cryptography']}, 9: {'World': ['property, socialist, negotiation, conspiracy, allegiance, imperialism, bloc, curfew, anarchism'], 'Sports': ['model, shot, youth, season, competition, defense, football, wrestling, puck'], 'Business': ['money, capital, stock, consumer, communications, commission, tourism, retail, broker'], 'Tech': ['use, value, systems, gold, technical, skill, psychology, primates, physic']}, 10: {'World': ['property, officer, federal, negotiation, petition, allegiance, clans, minimalist, anarchism, democrat'], 'Sports': ['model, event, shot, youth, season, defense, football, soccer, wrestling, puck'], 'Business': ['economic, resources, capital, stock, consumer, communications, transportation, retail, humanities, retailer'], 'Tech': ['value, systems, gold, networks, silver, skill, developer, transformer, primates, cryptography']}, 11: {'World': ['property, federal, negotiation, allegiance, imperialism, communism, senator, clans, minimalist, anarchism, democrat'], 'Sports': ['event, youth, season, competition, defense, television, football, cricket, tournament, wrestling, puck'], 'Business': ['money, market, capital, stock, agricultural, consumer, communications, commission, retail, dealer, broker'], 'Tech': ['use, value, systems, gold, technical, silver, devices, skill, psychology, transformer, primates']}, 12: {'World': ['political, property, officer, official, federal, ethics, tribes, petition, imperialism, curfew, anarchism, democrat'], 'Sports': ['event, average, youth, season, competition, defense, television, defence, football, tournament, wrestling, puck'], 'Business': ['money, economic, capital, labor, stock, purchase, agricultural, consumer, communications, retail, dealer, broker'], 'Tech': ['use, data, value, systems, gold, networks, silver, skill, mobile, transformer, primates, cryptography']}, 13: {'World': ['property, officer, official, expert, tribes, colonies, rebellion, petition, manipulation, imperialism, minimalist, anarchism, democrat'], 'Sports': ['event, average, shot, youth, season, competition, defense, television, defence, football, tournament, wrestling, puck'], 'Business': ['money, economic, services, capital, exchange, stock, agricultural, consumer, communications, broker, trades, retailer, interchange'], 'Tech': ['data, value, systems, strategy, gold, networks, silver, skill, productivity, developer, transformer, primates, cryptography']}, 14: {'World': ['company, property, officer, administration, ethics, tribes, rebellion, negotiation, petition, imperialism, bloc, curfew, anarchism, democrat'], 'Sports': ['event, average, shot, youth, season, competition, defense, television, defence, football, cricket, tournament, wrestling, puck'], 'Business': ['money, local, capital, stock, agricultural, communications, commission, tourism, shopping, retail, trades, wholesale, bureau, retailer'], 'Tech': ['use, data, value, systems, gold, applications, silver, devices, innovation, skill, telephone, transformer, primates, cryptography']}, 15: {'World': ['power, property, administration, election, tribes, negotiation, manipulation, allegiance, imperialism, communism, clans, bloc, minimalist, anarchism, democrat'], 'Sports': ['event, average, shot, youth, feature, competition, defense, television, defence, football, chess, boast, cricket, wrestling, puck'], 'Business': ['money, services, capital, exchange, stock, shop, consumer, communications, tourism, dealer, antique, dealings, bureau, forestry, retailer'], 'Tech': ['use, data, value, communication, gold, technical, silver, devices, skill, enterprise, productivity, telephone, networking, primates, cryptography']}, 16: {'World': ['power, property, administration, federal, expert, legislation, corruption, tribes, rebellion, negotiation, imperialism, communism, bloc, federation, anarchism, democrat'], 'Sports': ['event, average, shot, youth, feature, season, competition, defense, television, defence, football, boast, cricket, wrestling, hockey, volleyball'], 'Business': ['money, economic, capital, stock, department, traffic, agricultural, consumer, committee, tourism, commodity, retail, trades, trader, bureau, interchange'], 'Tech': ['use, data, value, gold, component, silver, devices, solutions, skill, enterprise, productivity, telephone, networking, technician, primates, cryptography']}, 17: {'World': ['power, property, administration, federal, expert, ideology, tribes, rebellion, coalition, negotiation, imperialism, communism, clans, bloc, federation, anarchism, democrat'], 'Sports': ['event, average, shot, youth, feature, competition, defense, television, defence, football, chess, boast, cricket, bout, wrestling, hockey, shooter'], 'Business': ['money, resources, capital, exchange, stock, traffic, payment, purchase, consumer, committee, communications, vice, export, retail, broker, dealings, trader'], 'Tech': ['data, value, systems, science, gold, silver, devices, innovation, skill, mobile, productivity, telephone, physics, complicate, transformer, primates, cryptography']}, 18: {'World': ['law, property, administration, federal, expert, legislation, tribes, rebellion, coalition, negotiation, imperialism, communism, senator, clans, minimalist, curfew, anarchism, democrat'], 'Sports': ['event, average, professional, shot, youth, feature, defense, television, defence, football, clubs, chess, boast, cricket, recreational, wrestling, shooter, dexterity'], 'Business': ['money, economic, services, resources, capital, exchange, labor, stock, sell, purchase, agricultural, communications, secretary, shopping, remainder, merchants, antique, bureau'], 'Tech': ['data, value, systems, design, gold, silver, devices, transformation, innovation, skill, mobile, club, psychology, weapon, productivity, telephone, primates, physic']}, 19: {'World': ['country, education, property, officer, administration, federal, ethics, tribes, socialist, coalition, petition, bureaucracy, allegiance, imperialism, clans, mislead, curfew, anarchism, democrat'], 'Sports': ['event, average, shot, youth, feature, defense, television, defence, football, clubs, soccer, chess, boast, cricket, wrestling, hockey, surf, dexterity, volleyball'], 'Business': ['money, resources, capital, stock, sell, traffic, purchase, commission, commerce, retail, buyer, entrepreneurship, antique, trades, merchandise, bureau, forestry, evasion, browse'], 'Tech': ['data, value, design, communication, gold, build, networks, component, silver, devices, skill, mobile, psychology, enterprise, productivity, telephone, networking, technician, primates']}, 20: {'World': ['power, law, city, property, administration, discourse, election, expert, ethics, tribes, rebellion, negotiation, manipulation, imperialism, communism, judiciary, clans, bloc, anarchism, democrat'], 'Sports': ['models, event, average, shot, youth, feature, defense, television, defence, football, clubs, golf, soccer, chess, cricket, recreational, wrestling, shooter, dexterity, esports'], 'Business': ['money, market, resources, capital, distribution, exchange, sector, stock, traffic, consumer, communications, remainder, retail, dealer, broker, dealings, forestry, browse, oversees, telecom'], 'Tech': ['data, value, science, communication, gold, networks, technical, silver, devices, skill, mobile, psychology, enterprise, productivity, telephone, expand, mathematics, networking, technician, primates']}}

        hypothesis_emo_synspace_LTOS = {2: {'World': ['profit expert'], 'Sports': ['football bob'], 'Business': ['capital prehistoric'], 'Tech': ['enterprise developer']}, 3: {'World': ['education officer federal'], 'Sports': ['football wage competitions'], 'Business': ['capital communications transportation'], 'Tech': ['gold computers developer']}, 4: {'World': ['education officer federal anarchism'], 'Sports': ['average defense wage competitions'], 'Business': ['capital stock communications transportation'], 'Tech': ['gold psychology enterprise robotics']}, 5: {'World': ['education tribute bloc minimalist anarchism'], 'Sports': ['model average competition defense recreational'], 'Business': ['money economic capital store stock'], 'Tech': ['gold skill psychology enterprise biomedical']}, 6: {'World': ['education property tribute bloc minimalist anarchism'], 'Sports': ['fun defense sports football golf puck'], 'Business': ['money resources capital stock consumer communications'], 'Tech': ['gold solutions skill productivity specialized developer']}, 7: {'World': ['property negotiation tribute allegiance bloc curfew anarchism'], 'Sports': ['competition defense television defence tournament wrestling puck'], 'Business': ['money economic capital stock consumer agriculture communications'], 'Tech': ['value gold solutions skill psychology specialized developer']}, 8: {'World': ['education property ethics petition manipulation tribute imperialism anarchism'], 'Sports': ['season defense defence golf soccer tournament wrestling puck'], 'Business': ['money resources capital stock consumer communications commission broker'], 'Tech': ['value communication gold skill specialized technician primates cryptography']}, 9: {'World': ['property socialist negotiation conspiracy allegiance imperialism bloc curfew anarchism'], 'Sports': ['model shot youth season competition defense football wrestling puck'], 'Business': ['money capital stock consumer communications commission tourism retail broker'], 'Tech': ['use value systems gold technical skill psychology primates physic']}, 10: {'World': ['property officer federal negotiation petition allegiance clans minimalist anarchism democrat'], 'Sports': ['model event shot youth season defense football soccer wrestling puck'], 'Business': ['economic resources capital stock consumer communications transportation retail humanities retailer'], 'Tech': ['value systems gold networks silver skill developer transformer primates cryptography']}, 11: {'World': ['property federal negotiation allegiance imperialism communism senator clans minimalist anarchism democrat'], 'Sports': ['event youth season competition defense television football cricket tournament wrestling puck'], 'Business': ['money market capital stock agricultural consumer communications commission retail dealer broker'], 'Tech': ['use value systems gold technical silver devices skill psychology transformer primates']}, 12: {'World': ['political property officer official federal ethics tribes petition imperialism curfew anarchism democrat'], 'Sports': ['event average youth season competition defense television defence football tournament wrestling puck'], 'Business': ['money economic capital labor stock purchase agricultural consumer communications retail dealer broker'], 'Tech': ['use data value systems gold networks silver skill mobile transformer primates cryptography']}, 13: {'World': ['property officer official expert tribes colonies rebellion petition manipulation imperialism minimalist anarchism democrat'], 'Sports': ['event average shot youth season competition defense television defence football tournament wrestling puck'], 'Business': ['money economic services capital exchange stock agricultural consumer communications broker trades retailer interchange'], 'Tech': ['data value systems strategy gold networks silver skill productivity developer transformer primates cryptography']}, 14: {'World': ['company property officer administration ethics tribes rebellion negotiation petition imperialism bloc curfew anarchism democrat'], 'Sports': ['event average shot youth season competition defense television defence football cricket tournament wrestling puck'], 'Business': ['money local capital stock agricultural communications commission tourism shopping retail trades wholesale bureau retailer'], 'Tech': ['use data value systems gold applications silver devices innovation skill telephone transformer primates cryptography']}, 15: {'World': ['power property administration election tribes negotiation manipulation allegiance imperialism communism clans bloc minimalist anarchism democrat'], 'Sports': ['event average shot youth feature competition defense television defence football chess boast cricket wrestling puck'], 'Business': ['money services capital exchange stock shop consumer communications tourism dealer antique dealings bureau forestry retailer'], 'Tech': ['use data value communication gold technical silver devices skill enterprise productivity telephone networking primates cryptography']}, 16: {'World': ['power property administration federal expert legislation corruption tribes rebellion negotiation imperialism communism bloc federation anarchism democrat'], 'Sports': ['event average shot youth feature season competition defense television defence football boast cricket wrestling hockey volleyball'], 'Business': ['money economic capital stock department traffic agricultural consumer committee tourism commodity retail trades trader bureau interchange'], 'Tech': ['use data value gold component silver devices solutions skill enterprise productivity telephone networking technician primates cryptography']}, 17: {'World': ['power property administration federal expert ideology tribes rebellion coalition negotiation imperialism communism clans bloc federation anarchism democrat'], 'Sports': ['event average shot youth feature competition defense television defence football chess boast cricket bout wrestling hockey shooter'], 'Business': ['money resources capital exchange stock traffic payment purchase consumer committee communications vice export retail broker dealings trader'], 'Tech': ['data value systems science gold silver devices innovation skill mobile productivity telephone physics complicate transformer primates cryptography']}, 18: {'World': ['law property administration federal expert legislation tribes rebellion coalition negotiation imperialism communism senator clans minimalist curfew anarchism democrat'], 'Sports': ['event average professional shot youth feature defense television defence football clubs chess boast cricket recreational wrestling shooter dexterity'], 'Business': ['money economic services resources capital exchange labor stock sell purchase agricultural communications secretary shopping remainder merchants antique bureau'], 'Tech': ['data value systems design gold silver devices transformation innovation skill mobile club psychology weapon productivity telephone primates physic']}, 19: {'World': ['country education property officer administration federal ethics tribes socialist coalition petition bureaucracy allegiance imperialism clans mislead curfew anarchism democrat'], 'Sports': ['event average shot youth feature defense television defence football clubs soccer chess boast cricket wrestling hockey surf dexterity volleyball'], 'Business': ['money resources capital stock sell traffic purchase commission commerce retail buyer entrepreneurship antique trades merchandise bureau forestry evasion browse'], 'Tech': ['data value design communication gold build networks component silver devices skill mobile psychology enterprise productivity telephone networking technician primates']}, 20: {'World': ['power law city property administration discourse election expert ethics tribes rebellion negotiation manipulation imperialism communism judiciary clans bloc anarchism democrat'], 'Sports': ['models event average shot youth feature defense television defence football clubs golf soccer chess cricket recreational wrestling shooter dexterity esports'], 'Business': ['money market resources capital distribution exchange sector stock traffic consumer communications remainder retail dealer broker dealings forestry browse oversees telecom'], 'Tech': ['data value science communication gold networks technical silver devices skill mobile psychology enterprise productivity telephone expand mathematics networking technician primates']}}

        hypothesis_emo_synslash_LTOS = {2: {'World': ['profit/ expert'], 'Sports': ['football/ bob'], 'Business': ['capital/ prehistoric'], 'Tech': ['enterprise/ developer']}, 3: {'World': ['education/ officer/ federal'], 'Sports': ['football/ wage/ competitions'], 'Business': ['capital/ communications/ transportation'], 'Tech': ['gold/ computers/ developer']}, 4: {'World': ['education/ officer/ federal/ anarchism'], 'Sports': ['average/ defense/ wage/ competitions'], 'Business': ['capital/ stock/ communications/ transportation'], 'Tech': ['gold/ psychology/ enterprise/ robotics']}, 5: {'World': ['education/ tribute/ bloc/ minimalist/ anarchism'], 'Sports': ['model/ average/ competition/ defense/ recreational'], 'Business': ['money/ economic/ capital/ store/ stock'], 'Tech': ['gold/ skill/ psychology/ enterprise/ biomedical']}, 6: {'World': ['education/ property/ tribute/ bloc/ minimalist/ anarchism'], 'Sports': ['fun/ defense/ sports/ football/ golf/ puck'], 'Business': ['money/ resources/ capital/ stock/ consumer/ communications'], 'Tech': ['gold/ solutions/ skill/ productivity/ specialized/ developer']}, 7: {'World': ['property/ negotiation/ tribute/ allegiance/ bloc/ curfew/ anarchism'], 'Sports': ['competition/ defense/ television/ defence/ tournament/ wrestling/ puck'], 'Business': ['money/ economic/ capital/ stock/ consumer/ agriculture/ communications'], 'Tech': ['value/ gold/ solutions/ skill/ psychology/ specialized/ developer']}, 8: {'World': ['education/ property/ ethics/ petition/ manipulation/ tribute/ imperialism/ anarchism'], 'Sports': ['season/ defense/ defence/ golf/ soccer/ tournament/ wrestling/ puck'], 'Business': ['money/ resources/ capital/ stock/ consumer/ communications/ commission/ broker'], 'Tech': ['value/ communication/ gold/ skill/ specialized/ technician/ primates/ cryptography']}, 9: {'World': ['property/ socialist/ negotiation/ conspiracy/ allegiance/ imperialism/ bloc/ curfew/ anarchism'], 'Sports': ['model/ shot/ youth/ season/ competition/ defense/ football/ wrestling/ puck'], 'Business': ['money/ capital/ stock/ consumer/ communications/ commission/ tourism/ retail/ broker'], 'Tech': ['use/ value/ systems/ gold/ technical/ skill/ psychology/ primates/ physic']}, 10: {'World': ['property/ officer/ federal/ negotiation/ petition/ allegiance/ clans/ minimalist/ anarchism/ democrat'], 'Sports': ['model/ event/ shot/ youth/ season/ defense/ football/ soccer/ wrestling/ puck'], 'Business': ['economic/ resources/ capital/ stock/ consumer/ communications/ transportation/ retail/ humanities/ retailer'], 'Tech': ['value/ systems/ gold/ networks/ silver/ skill/ developer/ transformer/ primates/ cryptography']}, 11: {'World': ['property/ federal/ negotiation/ allegiance/ imperialism/ communism/ senator/ clans/ minimalist/ anarchism/ democrat'], 'Sports': ['event/ youth/ season/ competition/ defense/ television/ football/ cricket/ tournament/ wrestling/ puck'], 'Business': ['money/ market/ capital/ stock/ agricultural/ consumer/ communications/ commission/ retail/ dealer/ broker'], 'Tech': ['use/ value/ systems/ gold/ technical/ silver/ devices/ skill/ psychology/ transformer/ primates']}, 12: {'World': ['political/ property/ officer/ official/ federal/ ethics/ tribes/ petition/ imperialism/ curfew/ anarchism/ democrat'], 'Sports': ['event/ average/ youth/ season/ competition/ defense/ television/ defence/ football/ tournament/ wrestling/ puck'], 'Business': ['money/ economic/ capital/ labor/ stock/ purchase/ agricultural/ consumer/ communications/ retail/ dealer/ broker'], 'Tech': ['use/ data/ value/ systems/ gold/ networks/ silver/ skill/ mobile/ transformer/ primates/ cryptography']}, 13: {'World': ['property/ officer/ official/ expert/ tribes/ colonies/ rebellion/ petition/ manipulation/ imperialism/ minimalist/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ season/ competition/ defense/ television/ defence/ football/ tournament/ wrestling/ puck'], 'Business': ['money/ economic/ services/ capital/ exchange/ stock/ agricultural/ consumer/ communications/ broker/ trades/ retailer/ interchange'], 'Tech': ['data/ value/ systems/ strategy/ gold/ networks/ silver/ skill/ productivity/ developer/ transformer/ primates/ cryptography']}, 14: {'World': ['company/ property/ officer/ administration/ ethics/ tribes/ rebellion/ negotiation/ petition/ imperialism/ bloc/ curfew/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ season/ competition/ defense/ television/ defence/ football/ cricket/ tournament/ wrestling/ puck'], 'Business': ['money/ local/ capital/ stock/ agricultural/ communications/ commission/ tourism/ shopping/ retail/ trades/ wholesale/ bureau/ retailer'], 'Tech': ['use/ data/ value/ systems/ gold/ applications/ silver/ devices/ innovation/ skill/ telephone/ transformer/ primates/ cryptography']}, 15: {'World': ['power/ property/ administration/ election/ tribes/ negotiation/ manipulation/ allegiance/ imperialism/ communism/ clans/ bloc/ minimalist/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ feature/ competition/ defense/ television/ defence/ football/ chess/ boast/ cricket/ wrestling/ puck'], 'Business': ['money/ services/ capital/ exchange/ stock/ shop/ consumer/ communications/ tourism/ dealer/ antique/ dealings/ bureau/ forestry/ retailer'], 'Tech': ['use/ data/ value/ communication/ gold/ technical/ silver/ devices/ skill/ enterprise/ productivity/ telephone/ networking/ primates/ cryptography']}, 16: {'World': ['power/ property/ administration/ federal/ expert/ legislation/ corruption/ tribes/ rebellion/ negotiation/ imperialism/ communism/ bloc/ federation/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ feature/ season/ competition/ defense/ television/ defence/ football/ boast/ cricket/ wrestling/ hockey/ volleyball'], 'Business': ['money/ economic/ capital/ stock/ department/ traffic/ agricultural/ consumer/ committee/ tourism/ commodity/ retail/ trades/ trader/ bureau/ interchange'], 'Tech': ['use/ data/ value/ gold/ component/ silver/ devices/ solutions/ skill/ enterprise/ productivity/ telephone/ networking/ technician/ primates/ cryptography']}, 17: {'World': ['power/ property/ administration/ federal/ expert/ ideology/ tribes/ rebellion/ coalition/ negotiation/ imperialism/ communism/ clans/ bloc/ federation/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ feature/ competition/ defense/ television/ defence/ football/ chess/ boast/ cricket/ bout/ wrestling/ hockey/ shooter'], 'Business': ['money/ resources/ capital/ exchange/ stock/ traffic/ payment/ purchase/ consumer/ committee/ communications/ vice/ export/ retail/ broker/ dealings/ trader'], 'Tech': ['data/ value/ systems/ science/ gold/ silver/ devices/ innovation/ skill/ mobile/ productivity/ telephone/ physics/ complicate/ transformer/ primates/ cryptography']}, 18: {'World': ['law/ property/ administration/ federal/ expert/ legislation/ tribes/ rebellion/ coalition/ negotiation/ imperialism/ communism/ senator/ clans/ minimalist/ curfew/ anarchism/ democrat'], 'Sports': ['event/ average/ professional/ shot/ youth/ feature/ defense/ television/ defence/ football/ clubs/ chess/ boast/ cricket/ recreational/ wrestling/ shooter/ dexterity'], 'Business': ['money/ economic/ services/ resources/ capital/ exchange/ labor/ stock/ sell/ purchase/ agricultural/ communications/ secretary/ shopping/ remainder/ merchants/ antique/ bureau'], 'Tech': ['data/ value/ systems/ design/ gold/ silver/ devices/ transformation/ innovation/ skill/ mobile/ club/ psychology/ weapon/ productivity/ telephone/ primates/ physic']}, 19: {'World': ['country/ education/ property/ officer/ administration/ federal/ ethics/ tribes/ socialist/ coalition/ petition/ bureaucracy/ allegiance/ imperialism/ clans/ mislead/ curfew/ anarchism/ democrat'], 'Sports': ['event/ average/ shot/ youth/ feature/ defense/ television/ defence/ football/ clubs/ soccer/ chess/ boast/ cricket/ wrestling/ hockey/ surf/ dexterity/ volleyball'], 'Business': ['money/ resources/ capital/ stock/ sell/ traffic/ purchase/ commission/ commerce/ retail/ buyer/ entrepreneurship/ antique/ trades/ merchandise/ bureau/ forestry/ evasion/ browse'], 'Tech': ['data/ value/ design/ communication/ gold/ build/ networks/ component/ silver/ devices/ skill/ mobile/ psychology/ enterprise/ productivity/ telephone/ networking/ technician/ primates']}, 20: {'World': ['power/ law/ city/ property/ administration/ discourse/ election/ expert/ ethics/ tribes/ rebellion/ negotiation/ manipulation/ imperialism/ communism/ judiciary/ clans/ bloc/ anarchism/ democrat'], 'Sports': ['models/ event/ average/ shot/ youth/ feature/ defense/ television/ defence/ football/ clubs/ golf/ soccer/ chess/ cricket/ recreational/ wrestling/ shooter/ dexterity/ esports'], 'Business': ['money/ market/ resources/ capital/ distribution/ exchange/ sector/ stock/ traffic/ consumer/ communications/ remainder/ retail/ dealer/ broker/ dealings/ forestry/ browse/ oversees/ telecom'], 'Tech': ['data/ value/ science/ communication/ gold/ networks/ technical/ silver/ devices/ skill/ mobile/ psychology/ enterprise/ productivity/ telephone/ expand/ mathematics/ networking/ technician/ primates']}}


        hypothesis_emo_synsand_LTOS = {2: {'World': ['profit and expert'], 'Sports': ['football and bob'], 'Business': ['capital and prehistoric'], 'Tech': ['enterprise and developer']}, 3: {'World': ['education and officer and federal'], 'Sports': ['football and wage and competitions'], 'Business': ['capital and communications and transportation'], 'Tech': ['gold and computers and developer']}, 4: {'World': ['education and officer and federal and anarchism'], 'Sports': ['average and defense and wage and competitions'], 'Business': ['capital and stock and communications and transportation'], 'Tech': ['gold and psychology and enterprise and robotics']}, 5: {'World': ['education and tribute and bloc and minimalist and anarchism'], 'Sports': ['model and average and competition and defense and recreational'], 'Business': ['money and economic and capital and store and stock'], 'Tech': ['gold and skill and psychology and enterprise and biomedical']}, 6: {'World': ['education and property and tribute and bloc and minimalist and anarchism'], 'Sports': ['fun and defense and sports and football and golf and puck'], 'Business': ['money and resources and capital and stock and consumer and communications'], 'Tech': ['gold and solutions and skill and productivity and specialized and developer']}, 7: {'World': ['property and negotiation and tribute and allegiance and bloc and curfew and anarchism'], 'Sports': ['competition and defense and television and defence and tournament and wrestling and puck'], 'Business': ['money and economic and capital and stock and consumer and agriculture and communications'], 'Tech': ['value and gold and solutions and skill and psychology and specialized and developer']}, 8: {'World': ['education and property and ethics and petition and manipulation and tribute and imperialism and anarchism'], 'Sports': ['season and defense and defence and golf and soccer and tournament and wrestling and puck'], 'Business': ['money and resources and capital and stock and consumer and communications and commission and broker'], 'Tech': ['value and communication and gold and skill and specialized and technician and primates and cryptography']}, 9: {'World': ['property and socialist and negotiation and conspiracy and allegiance and imperialism and bloc and curfew and anarchism'], 'Sports': ['model and shot and youth and season and competition and defense and football and wrestling and puck'], 'Business': ['money and capital and stock and consumer and communications and commission and tourism and retail and broker'], 'Tech': ['use and value and systems and gold and technical and skill and psychology and primates and physic']}, 10: {'World': ['property and officer and federal and negotiation and petition and allegiance and clans and minimalist and anarchism and democrat'], 'Sports': ['model and event and shot and youth and season and defense and football and soccer and wrestling and puck'], 'Business': ['economic and resources and capital and stock and consumer and communications and transportation and retail and humanities and retailer'], 'Tech': ['value and systems and gold and networks and silver and skill and developer and transformer and primates and cryptography']}, 11: {'World': ['property and federal and negotiation and allegiance and imperialism and communism and senator and clans and minimalist and anarchism and democrat'], 'Sports': ['event and youth and season and competition and defense and television and football and cricket and tournament and wrestling and puck'], 'Business': ['money and market and capital and stock and agricultural and consumer and communications and commission and retail and dealer and broker'], 'Tech': ['use and value and systems and gold and technical and silver and devices and skill and psychology and transformer and primates']}, 12: {'World': ['political and property and officer and official and federal and ethics and tribes and petition and imperialism and curfew and anarchism and democrat'], 'Sports': ['event and average and youth and season and competition and defense and television and defence and football and tournament and wrestling and puck'], 'Business': ['money and economic and capital and labor and stock and purchase and agricultural and consumer and communications and retail and dealer and broker'], 'Tech': ['use and data and value and systems and gold and networks and silver and skill and mobile and transformer and primates and cryptography']}, 13: {'World': ['property and officer and official and expert and tribes and colonies and rebellion and petition and manipulation and imperialism and minimalist and anarchism and democrat'], 'Sports': ['event and average and shot and youth and season and competition and defense and television and defence and football and tournament and wrestling and puck'], 'Business': ['money and economic and services and capital and exchange and stock and agricultural and consumer and communications and broker and trades and retailer and interchange'], 'Tech': ['data and value and systems and strategy and gold and networks and silver and skill and productivity and developer and transformer and primates and cryptography']}, 14: {'World': ['company and property and officer and administration and ethics and tribes and rebellion and negotiation and petition and imperialism and bloc and curfew and anarchism and democrat'], 'Sports': ['event and average and shot and youth and season and competition and defense and television and defence and football and cricket and tournament and wrestling and puck'], 'Business': ['money and local and capital and stock and agricultural and communications and commission and tourism and shopping and retail and trades and wholesale and bureau and retailer'], 'Tech': ['use and data and value and systems and gold and applications and silver and devices and innovation and skill and telephone and transformer and primates and cryptography']}, 15: {'World': ['power and property and administration and election and tribes and negotiation and manipulation and allegiance and imperialism and communism and clans and bloc and minimalist and anarchism and democrat'], 'Sports': ['event and average and shot and youth and feature and competition and defense and television and defence and football and chess and boast and cricket and wrestling and puck'], 'Business': ['money and services and capital and exchange and stock and shop and consumer and communications and tourism and dealer and antique and dealings and bureau and forestry and retailer'], 'Tech': ['use and data and value and communication and gold and technical and silver and devices and skill and enterprise and productivity and telephone and networking and primates and cryptography']}, 16: {'World': ['power and property and administration and federal and expert and legislation and corruption and tribes and rebellion and negotiation and imperialism and communism and bloc and federation and anarchism and democrat'], 'Sports': ['event and average and shot and youth and feature and season and competition and defense and television and defence and football and boast and cricket and wrestling and hockey and volleyball'], 'Business': ['money and economic and capital and stock and department and traffic and agricultural and consumer and committee and tourism and commodity and retail and trades and trader and bureau and interchange'], 'Tech': ['use and data and value and gold and component and silver and devices and solutions and skill and enterprise and productivity and telephone and networking and technician and primates and cryptography']}, 17: {'World': ['power and property and administration and federal and expert and ideology and tribes and rebellion and coalition and negotiation and imperialism and communism and clans and bloc and federation and anarchism and democrat'], 'Sports': ['event and average and shot and youth and feature and competition and defense and television and defence and football and chess and boast and cricket and bout and wrestling and hockey and shooter'], 'Business': ['money and resources and capital and exchange and stock and traffic and payment and purchase and consumer and committee and communications and vice and export and retail and broker and dealings and trader'], 'Tech': ['data and value and systems and science and gold and silver and devices and innovation and skill and mobile and productivity and telephone and physics and complicate and transformer and primates and cryptography']}, 18: {'World': ['law and property and administration and federal and expert and legislation and tribes and rebellion and coalition and negotiation and imperialism and communism and senator and clans and minimalist and curfew and anarchism and democrat'], 'Sports': ['event and average and professional and shot and youth and feature and defense and television and defence and football and clubs and chess and boast and cricket and recreational and wrestling and shooter and dexterity'], 'Business': ['money and economic and services and resources and capital and exchange and labor and stock and sell and purchase and agricultural and communications and secretary and shopping and remainder and merchants and antique and bureau'], 'Tech': ['data and value and systems and design and gold and silver and devices and transformation and innovation and skill and mobile and club and psychology and weapon and productivity and telephone and primates and physic']}, 19: {'World': ['country and education and property and officer and administration and federal and ethics and tribes and socialist and coalition and petition and bureaucracy and allegiance and imperialism and clans and mislead and curfew and anarchism and democrat'], 'Sports': ['event and average and shot and youth and feature and defense and television and defence and football and clubs and soccer and chess and boast and cricket and wrestling and hockey and surf and dexterity and volleyball'], 'Business': ['money and resources and capital and stock and sell and traffic and purchase and commission and commerce and retail and buyer and entrepreneurship and antique and trades and merchandise and bureau and forestry and evasion and browse'], 'Tech': ['data and value and design and communication and gold and build and networks and component and silver and devices and skill and mobile and psychology and enterprise and productivity and telephone and networking and technician and primates']}, 20: {'World': ['power and law and city and property and administration and discourse and election and expert and ethics and tribes and rebellion and negotiation and manipulation and imperialism and communism and judiciary and clans and bloc and anarchism and democrat'], 'Sports': ['models and event and average and shot and youth and feature and defense and television and defence and football and clubs and golf and soccer and chess and cricket and recreational and wrestling and shooter and dexterity and esports'], 'Business': ['money and market and resources and capital and distribution and exchange and sector and stock and traffic and consumer and communications and remainder and retail and dealer and broker and dealings and forestry and browse and oversees and telecom'], 'Tech': ['data and value and science and communication and gold and networks and technical and silver and devices and skill and mobile and psychology and enterprise and productivity and telephone and expand and mathematics and networking and technician and primates']}}

    else:
        hypothesis_emo_syns_LTOS ={2: {'World': ['expert, profit'], 'Sports': ['bob, football'], 'Business': ['capital, prehistoric'], 'Tech': ['developer, enterprise']}, 3: {'World': ['officer, federal, education'], 'Sports': ['competitions, wage, football'], 'Business': ['capital, communications, transportation'], 'Tech': ['computers, developer, gold']}, 4: {'World': ['officer, federal, education, anarchism'], 'Sports': ['competitions, wage, defense, average'], 'Business': ['stock, capital, communications, transportation'], 'Tech': ['enterprise, psychology, gold, robotics']}, 5: {'World': ['bloc, tribute, education, anarchism, minimalist'], 'Sports': ['competition, defense, recreational, model, average'], 'Business': ['stock, capital, money, store, economic'], 'Tech': ['enterprise, skill, biomedical, psychology, gold']}, 6: {'World': ['bloc, property, tribute, education, anarchism, minimalist'], 'Sports': ['sports, defense, football, puck, fun, golf'], 'Business': ['stock, capital, money, resources, consumer, communications'], 'Tech': ['specialized, solutions, developer, skill, productivity, gold']}, 7: {'World': ['bloc, negotiation, property, allegiance, curfew, tribute, anarchism'], 'Sports': ['competition, tournament, defense, defence, television, puck, wrestling'], 'Business': ['stock, capital, money, consumer, economic, communications, agriculture'], 'Tech': ['specialized, solutions, value, developer, skill, psychology, gold']}, 8: {'World': ['property, manipulation, petition, ethics, tribute, imperialism, education, anarchism'], 'Sports': ['tournament, season, defense, defence, puck, soccer, golf, wrestling'], 'Business': ['stock, broker, capital, money, resources, commission, consumer, communications'], 'Tech': ['specialized, communication, value, technician, skill, cryptography, primates, gold']}, 9: {'World': ['bloc, negotiation, property, allegiance, curfew, imperialism, socialist, conspiracy, anarchism'], 'Sports': ['competition, shot, season, defense, model, football, youth, puck, wrestling'], 'Business': ['stock, broker, capital, money, commission, consumer, communications, retail, tourism'], 'Tech': ['use, systems, technical, value, physic, skill, psychology, primates, gold']}, 10: {'World': ['officer, negotiation, federal, property, allegiance, petition, clans, democrat, anarchism, minimalist'], 'Sports': ['event, shot, season, defense, model, football, youth, puck, soccer, wrestling'], 'Business': ['stock, capital, resources, consumer, economic, communications, retailer, humanities, transportation, retail'], 'Tech': ['systems, transformer, value, developer, skill, networks, cryptography, primates, gold, silver']}, 11: {'World': ['negotiation, senator, federal, property, allegiance, clans, communism, democrat, imperialism, anarchism, minimalist'], 'Sports': ['event, competition, tournament, season, defense, television, football, youth, puck, cricket, wrestling'], 'Business': ['stock, market, dealer, broker, capital, money, commission, consumer, communications, retail, agricultural'], 'Tech': ['use, systems, technical, devices, transformer, value, skill, psychology, primates, gold, silver']}, 12: {'World': ['official, officer, federal, political, property, petition, curfew, ethics, tribes, democrat, imperialism, anarchism'], 'Sports': ['event, competition, tournament, season, defense, defence, television, football, average, youth, puck, wrestling'], 'Business': ['stock, dealer, purchase, broker, capital, money, consumer, economic, communications, labor, retail, agricultural'], 'Tech': ['use, systems, transformer, value, skill, data, networks, mobile, cryptography, primates, gold, silver']}, 13: {'World': ['official, expert, officer, rebellion, property, manipulation, petition, colonies, tribes, democrat, imperialism, anarchism, minimalist'], 'Sports': ['event, competition, shot, tournament, season, defense, defence, television, football, average, youth, puck, wrestling'], 'Business': ['stock, interchange, exchange, trades, broker, capital, money, consumer, economic, communications, services, retailer, agricultural'], 'Tech': ['systems, transformer, value, developer, strategy, skill, data, networks, productivity, cryptography, primates, gold, silver']}, 14: {'World': ['bloc, officer, negotiation, rebellion, property, company, petition, administration, curfew, ethics, tribes, democrat, imperialism, anarchism'], 'Sports': ['event, competition, shot, tournament, season, defense, defence, television, football, average, youth, puck, cricket, wrestling'], 'Business': ['bureau, stock, trades, capital, money, wholesale, commission, local, communications, retailer, retail, shopping, tourism, agricultural'], 'Tech': ['use, systems, devices, transformer, value, applications, skill, innovation, data, cryptography, telephone, primates, gold, silver']}, 15: {'World': ['bloc, power, negotiation, property, allegiance, manipulation, clans, administration, tribes, communism, democrat, imperialism, election, anarchism, minimalist'], 'Sports': ['event, competition, shot, feature, boast, defense, defence, television, football, average, youth, puck, chess, cricket, wrestling'], 'Business': ['bureau, stock, dealer, exchange, capital, money, dealings, shop, consumer, communications, services, retailer, forestry, antique, tourism'], 'Tech': ['use, technical, devices, communication, value, enterprise, skill, data, networking, productivity, cryptography, telephone, primates, gold, silver']}, 16: {'World': ['bloc, expert, power, federation, negotiation, federal, rebellion, property, administration, legislation, tribes, communism, democrat, imperialism, anarchism, corruption'], 'Sports': ['event, competition, shot, feature, season, boast, defense, defence, television, football, average, youth, hockey, cricket, volleyball, wrestling'], 'Business': ['bureau, department, stock, committee, interchange, trades, capital, money, trader, consumer, commodity, economic, retail, traffic, tourism, agricultural'], 'Tech': ['component, use, devices, solutions, value, enterprise, technician, skill, data, networking, productivity, cryptography, telephone, primates, gold, silver']}, 17: {'World': ['bloc, expert, power, federation, negotiation, coalition, federal, rebellion, property, clans, administration, ideology, tribes, communism, democrat, imperialism, anarchism'], 'Sports': ['event, competition, bout, shot, feature, boast, shooter, defense, defence, television, football, average, youth, hockey, chess, cricket, wrestling'], 'Business': ['stock, committee, exchange, purchase, broker, capital, money, dealings, payment, export, trader, resources, consumer, communications, vice, retail, traffic'], 'Tech': ['systems, devices, transformer, complicate, value, skill, innovation, data, mobile, science, productivity, cryptography, telephone, primates, gold, silver, physics']}, 18: {'World': ['expert, negotiation, senator, coalition, federal, rebellion, property, law, clans, administration, legislation, curfew, tribes, communism, democrat, imperialism, anarchism, minimalist'], 'Sports': ['event, shot, feature, professional, clubs, boast, shooter, defense, dexterity, defence, television, recreational, football, average, youth, chess, cricket, wrestling'], 'Business': ['remainder, bureau, stock, exchange, purchase, secretary, capital, money, resources, sell, economic, communications, services, merchants, labor, antique, shopping, agricultural'], 'Tech': ['systems, devices, transformation, value, physic, skill, innovation, data, club, mobile, weapon, design, psychology, productivity, telephone, primates, gold, silver']}, 19: {'World': ['country, officer, coalition, federal, property, mislead, allegiance, petition, clans, administration, curfew, ethics, tribes, democrat, imperialism, bureaucracy, socialist, education, anarchism'], 'Sports': ['event, shot, feature, clubs, boast, defense, dexterity, defence, television, football, average, youth, soccer, hockey, chess, surf, cricket, volleyball, wrestling'], 'Business': ['bureau, browse, stock, buyer, purchase, trades, capital, money, resources, commission, sell, commerce, entrepreneurship, merchandise, evasion, forestry, retail, antique, traffic'], 'Tech': ['component, devices, build, communication, value, enterprise, technician, skill, data, networks, mobile, design, networking, psychology, productivity, telephone, primates, gold, silver']}, 20: {'World': ['discourse, bloc, expert, city, power, negotiation, rebellion, property, law, manipulation, judiciary, clans, administration, ethics, tribes, communism, democrat, imperialism, election, anarchism'], 'Sports': ['event, shot, feature, clubs, shooter, defense, dexterity, defence, television, recreational, football, models, average, esports, youth, soccer, golf, chess, cricket, wrestling'], 'Business': ['remainder, oversees, browse, sector, stock, market, dealer, exchange, broker, capital, money, dealings, resources, consumer, distribution, communications, forestry, retail, telecom, traffic'], 'Tech': ['expand, technical, devices, communication, value, enterprise, technician, skill, data, networks, mobile, networking, psychology, science, productivity, telephone, mathematics, primates, gold, silver']}}

        hypothesis_emo_synspace_LTOS ={2: {'World': ['expert profit'], 'Sports': ['bob football'], 'Business': ['capital prehistoric'], 'Tech': ['developer enterprise']}, 3: {'World': ['officer federal education'], 'Sports': ['competitions wage football'], 'Business': ['capital communications transportation'], 'Tech': ['computers developer gold']}, 4: {'World': ['officer federal education anarchism'], 'Sports': ['competitions wage defense average'], 'Business': ['stock capital communications transportation'], 'Tech': ['enterprise psychology gold robotics']}, 5: {'World': ['bloc tribute education anarchism minimalist'], 'Sports': ['competition defense recreational model average'], 'Business': ['stock capital money store economic'], 'Tech': ['enterprise skill biomedical psychology gold']}, 6: {'World': ['bloc property tribute education anarchism minimalist'], 'Sports': ['sports defense football puck fun golf'], 'Business': ['stock capital money resources consumer communications'], 'Tech': ['specialized solutions developer skill productivity gold']}, 7: {'World': ['bloc negotiation property allegiance curfew tribute anarchism'], 'Sports': ['competition tournament defense defence television puck wrestling'], 'Business': ['stock capital money consumer economic communications agriculture'], 'Tech': ['specialized solutions value developer skill psychology gold']}, 8: {'World': ['property manipulation petition ethics tribute imperialism education anarchism'], 'Sports': ['tournament season defense defence puck soccer golf wrestling'], 'Business': ['stock broker capital money resources commission consumer communications'], 'Tech': ['specialized communication value technician skill cryptography primates gold']}, 9: {'World': ['bloc negotiation property allegiance curfew imperialism socialist conspiracy anarchism'], 'Sports': ['competition shot season defense model football youth puck wrestling'], 'Business': ['stock broker capital money commission consumer communications retail tourism'], 'Tech': ['use systems technical value physic skill psychology primates gold']}, 10: {'World': ['officer negotiation federal property allegiance petition clans democrat anarchism minimalist'], 'Sports': ['event shot season defense model football youth puck soccer wrestling'], 'Business': ['stock capital resources consumer economic communications retailer humanities transportation retail'], 'Tech': ['systems transformer value developer skill networks cryptography primates gold silver']}, 11: {'World': ['negotiation senator federal property allegiance clans communism democrat imperialism anarchism minimalist'], 'Sports': ['event competition tournament season defense television football youth puck cricket wrestling'], 'Business': ['stock market dealer broker capital money commission consumer communications retail agricultural'], 'Tech': ['use systems technical devices transformer value skill psychology primates gold silver']}, 12: {'World': ['official officer federal political property petition curfew ethics tribes democrat imperialism anarchism'], 'Sports': ['event competition tournament season defense defence television football average youth puck wrestling'], 'Business': ['stock dealer purchase broker capital money consumer economic communications labor retail agricultural'], 'Tech': ['use systems transformer value skill data networks mobile cryptography primates gold silver']}, 13: {'World': ['official expert officer rebellion property manipulation petition colonies tribes democrat imperialism anarchism minimalist'], 'Sports': ['event competition shot tournament season defense defence television football average youth puck wrestling'], 'Business': ['stock interchange exchange trades broker capital money consumer economic communications services retailer agricultural'], 'Tech': ['systems transformer value developer strategy skill data networks productivity cryptography primates gold silver']}, 14: {'World': ['bloc officer negotiation rebellion property company petition administration curfew ethics tribes democrat imperialism anarchism'], 'Sports': ['event competition shot tournament season defense defence television football average youth puck cricket wrestling'], 'Business': ['bureau stock trades capital money wholesale commission local communications retailer retail shopping tourism agricultural'], 'Tech': ['use systems devices transformer value applications skill innovation data cryptography telephone primates gold silver']}, 15: {'World': ['bloc power negotiation property allegiance manipulation clans administration tribes communism democrat imperialism election anarchism minimalist'], 'Sports': ['event competition shot feature boast defense defence television football average youth puck chess cricket wrestling'], 'Business': ['bureau stock dealer exchange capital money dealings shop consumer communications services retailer forestry antique tourism'], 'Tech': ['use technical devices communication value enterprise skill data networking productivity cryptography telephone primates gold silver']}, 16: {'World': ['bloc expert power federation negotiation federal rebellion property administration legislation tribes communism democrat imperialism anarchism corruption'], 'Sports': ['event competition shot feature season boast defense defence television football average youth hockey cricket volleyball wrestling'], 'Business': ['bureau department stock committee interchange trades capital money trader consumer commodity economic retail traffic tourism agricultural'], 'Tech': ['component use devices solutions value enterprise technician skill data networking productivity cryptography telephone primates gold silver']}, 17: {'World': ['bloc expert power federation negotiation coalition federal rebellion property clans administration ideology tribes communism democrat imperialism anarchism'], 'Sports': ['event competition bout shot feature boast shooter defense defence television football average youth hockey chess cricket wrestling'], 'Business': ['stock committee exchange purchase broker capital money dealings payment export trader resources consumer communications vice retail traffic'], 'Tech': ['systems devices transformer complicate value skill innovation data mobile science productivity cryptography telephone primates gold silver physics']}, 18: {'World': ['expert negotiation senator coalition federal rebellion property law clans administration legislation curfew tribes communism democrat imperialism anarchism minimalist'], 'Sports': ['event shot feature professional clubs boast shooter defense dexterity defence television recreational football average youth chess cricket wrestling'], 'Business': ['remainder bureau stock exchange purchase secretary capital money resources sell economic communications services merchants labor antique shopping agricultural'], 'Tech': ['systems devices transformation value physic skill innovation data club mobile weapon design psychology productivity telephone primates gold silver']}, 19: {'World': ['country officer coalition federal property mislead allegiance petition clans administration curfew ethics tribes democrat imperialism bureaucracy socialist education anarchism'], 'Sports': ['event shot feature clubs boast defense dexterity defence television football average youth soccer hockey chess surf cricket volleyball wrestling'], 'Business': ['bureau browse stock buyer purchase trades capital money resources commission sell commerce entrepreneurship merchandise evasion forestry retail antique traffic'], 'Tech': ['component devices build communication value enterprise technician skill data networks mobile design networking psychology productivity telephone primates gold silver']}, 20: {'World': ['discourse bloc expert city power negotiation rebellion property law manipulation judiciary clans administration ethics tribes communism democrat imperialism election anarchism'], 'Sports': ['event shot feature clubs shooter defense dexterity defence television recreational football models average esports youth soccer golf chess cricket wrestling'], 'Business': ['remainder oversees browse sector stock market dealer exchange broker capital money dealings resources consumer distribution communications forestry retail telecom traffic'], 'Tech': ['expand technical devices communication value enterprise technician skill data networks mobile networking psychology science productivity telephone mathematics primates gold silver']}}

        hypothesis_emo_synslash_LTOS ={2: {'World': ['expert/ profit'], 'Sports': ['bob/ football'], 'Business': ['capital/ prehistoric'], 'Tech': ['developer/ enterprise']}, 3: {'World': ['officer/ federal/ education'], 'Sports': ['competitions/ wage/ football'], 'Business': ['capital/ communications/ transportation'], 'Tech': ['computers/ developer/ gold']}, 4: {'World': ['officer/ federal/ education/ anarchism'], 'Sports': ['competitions/ wage/ defense/ average'], 'Business': ['stock/ capital/ communications/ transportation'], 'Tech': ['enterprise/ psychology/ gold/ robotics']}, 5: {'World': ['bloc/ tribute/ education/ anarchism/ minimalist'], 'Sports': ['competition/ defense/ recreational/ model/ average'], 'Business': ['stock/ capital/ money/ store/ economic'], 'Tech': ['enterprise/ skill/ biomedical/ psychology/ gold']}, 6: {'World': ['bloc/ property/ tribute/ education/ anarchism/ minimalist'], 'Sports': ['sports/ defense/ football/ puck/ fun/ golf'], 'Business': ['stock/ capital/ money/ resources/ consumer/ communications'], 'Tech': ['specialized/ solutions/ developer/ skill/ productivity/ gold']}, 7: {'World': ['bloc/ negotiation/ property/ allegiance/ curfew/ tribute/ anarchism'], 'Sports': ['competition/ tournament/ defense/ defence/ television/ puck/ wrestling'], 'Business': ['stock/ capital/ money/ consumer/ economic/ communications/ agriculture'], 'Tech': ['specialized/ solutions/ value/ developer/ skill/ psychology/ gold']}, 8: {'World': ['property/ manipulation/ petition/ ethics/ tribute/ imperialism/ education/ anarchism'], 'Sports': ['tournament/ season/ defense/ defence/ puck/ soccer/ golf/ wrestling'], 'Business': ['stock/ broker/ capital/ money/ resources/ commission/ consumer/ communications'], 'Tech': ['specialized/ communication/ value/ technician/ skill/ cryptography/ primates/ gold']}, 9: {'World': ['bloc/ negotiation/ property/ allegiance/ curfew/ imperialism/ socialist/ conspiracy/ anarchism'], 'Sports': ['competition/ shot/ season/ defense/ model/ football/ youth/ puck/ wrestling'], 'Business': ['stock/ broker/ capital/ money/ commission/ consumer/ communications/ retail/ tourism'], 'Tech': ['use/ systems/ technical/ value/ physic/ skill/ psychology/ primates/ gold']}, 10: {'World': ['officer/ negotiation/ federal/ property/ allegiance/ petition/ clans/ democrat/ anarchism/ minimalist'], 'Sports': ['event/ shot/ season/ defense/ model/ football/ youth/ puck/ soccer/ wrestling'], 'Business': ['stock/ capital/ resources/ consumer/ economic/ communications/ retailer/ humanities/ transportation/ retail'], 'Tech': ['systems/ transformer/ value/ developer/ skill/ networks/ cryptography/ primates/ gold/ silver']}, 11: {'World': ['negotiation/ senator/ federal/ property/ allegiance/ clans/ communism/ democrat/ imperialism/ anarchism/ minimalist'], 'Sports': ['event/ competition/ tournament/ season/ defense/ television/ football/ youth/ puck/ cricket/ wrestling'], 'Business': ['stock/ market/ dealer/ broker/ capital/ money/ commission/ consumer/ communications/ retail/ agricultural'], 'Tech': ['use/ systems/ technical/ devices/ transformer/ value/ skill/ psychology/ primates/ gold/ silver']}, 12: {'World': ['official/ officer/ federal/ political/ property/ petition/ curfew/ ethics/ tribes/ democrat/ imperialism/ anarchism'], 'Sports': ['event/ competition/ tournament/ season/ defense/ defence/ television/ football/ average/ youth/ puck/ wrestling'], 'Business': ['stock/ dealer/ purchase/ broker/ capital/ money/ consumer/ economic/ communications/ labor/ retail/ agricultural'], 'Tech': ['use/ systems/ transformer/ value/ skill/ data/ networks/ mobile/ cryptography/ primates/ gold/ silver']}, 13: {'World': ['official/ expert/ officer/ rebellion/ property/ manipulation/ petition/ colonies/ tribes/ democrat/ imperialism/ anarchism/ minimalist'], 'Sports': ['event/ competition/ shot/ tournament/ season/ defense/ defence/ television/ football/ average/ youth/ puck/ wrestling'], 'Business': ['stock/ interchange/ exchange/ trades/ broker/ capital/ money/ consumer/ economic/ communications/ services/ retailer/ agricultural'], 'Tech': ['systems/ transformer/ value/ developer/ strategy/ skill/ data/ networks/ productivity/ cryptography/ primates/ gold/ silver']}, 14: {'World': ['bloc/ officer/ negotiation/ rebellion/ property/ company/ petition/ administration/ curfew/ ethics/ tribes/ democrat/ imperialism/ anarchism'], 'Sports': ['event/ competition/ shot/ tournament/ season/ defense/ defence/ television/ football/ average/ youth/ puck/ cricket/ wrestling'], 'Business': ['bureau/ stock/ trades/ capital/ money/ wholesale/ commission/ local/ communications/ retailer/ retail/ shopping/ tourism/ agricultural'], 'Tech': ['use/ systems/ devices/ transformer/ value/ applications/ skill/ innovation/ data/ cryptography/ telephone/ primates/ gold/ silver']}, 15: {'World': ['bloc/ power/ negotiation/ property/ allegiance/ manipulation/ clans/ administration/ tribes/ communism/ democrat/ imperialism/ election/ anarchism/ minimalist'], 'Sports': ['event/ competition/ shot/ feature/ boast/ defense/ defence/ television/ football/ average/ youth/ puck/ chess/ cricket/ wrestling'], 'Business': ['bureau/ stock/ dealer/ exchange/ capital/ money/ dealings/ shop/ consumer/ communications/ services/ retailer/ forestry/ antique/ tourism'], 'Tech': ['use/ technical/ devices/ communication/ value/ enterprise/ skill/ data/ networking/ productivity/ cryptography/ telephone/ primates/ gold/ silver']}, 16: {'World': ['bloc/ expert/ power/ federation/ negotiation/ federal/ rebellion/ property/ administration/ legislation/ tribes/ communism/ democrat/ imperialism/ anarchism/ corruption'], 'Sports': ['event/ competition/ shot/ feature/ season/ boast/ defense/ defence/ television/ football/ average/ youth/ hockey/ cricket/ volleyball/ wrestling'], 'Business': ['bureau/ department/ stock/ committee/ interchange/ trades/ capital/ money/ trader/ consumer/ commodity/ economic/ retail/ traffic/ tourism/ agricultural'], 'Tech': ['component/ use/ devices/ solutions/ value/ enterprise/ technician/ skill/ data/ networking/ productivity/ cryptography/ telephone/ primates/ gold/ silver']}, 17: {'World': ['bloc/ expert/ power/ federation/ negotiation/ coalition/ federal/ rebellion/ property/ clans/ administration/ ideology/ tribes/ communism/ democrat/ imperialism/ anarchism'], 'Sports': ['event/ competition/ bout/ shot/ feature/ boast/ shooter/ defense/ defence/ television/ football/ average/ youth/ hockey/ chess/ cricket/ wrestling'], 'Business': ['stock/ committee/ exchange/ purchase/ broker/ capital/ money/ dealings/ payment/ export/ trader/ resources/ consumer/ communications/ vice/ retail/ traffic'], 'Tech': ['systems/ devices/ transformer/ complicate/ value/ skill/ innovation/ data/ mobile/ science/ productivity/ cryptography/ telephone/ primates/ gold/ silver/ physics']}, 18: {'World': ['expert/ negotiation/ senator/ coalition/ federal/ rebellion/ property/ law/ clans/ administration/ legislation/ curfew/ tribes/ communism/ democrat/ imperialism/ anarchism/ minimalist'], 'Sports': ['event/ shot/ feature/ professional/ clubs/ boast/ shooter/ defense/ dexterity/ defence/ television/ recreational/ football/ average/ youth/ chess/ cricket/ wrestling'], 'Business': ['remainder/ bureau/ stock/ exchange/ purchase/ secretary/ capital/ money/ resources/ sell/ economic/ communications/ services/ merchants/ labor/ antique/ shopping/ agricultural'], 'Tech': ['systems/ devices/ transformation/ value/ physic/ skill/ innovation/ data/ club/ mobile/ weapon/ design/ psychology/ productivity/ telephone/ primates/ gold/ silver']}, 19: {'World': ['country/ officer/ coalition/ federal/ property/ mislead/ allegiance/ petition/ clans/ administration/ curfew/ ethics/ tribes/ democrat/ imperialism/ bureaucracy/ socialist/ education/ anarchism'], 'Sports': ['event/ shot/ feature/ clubs/ boast/ defense/ dexterity/ defence/ television/ football/ average/ youth/ soccer/ hockey/ chess/ surf/ cricket/ volleyball/ wrestling'], 'Business': ['bureau/ browse/ stock/ buyer/ purchase/ trades/ capital/ money/ resources/ commission/ sell/ commerce/ entrepreneurship/ merchandise/ evasion/ forestry/ retail/ antique/ traffic'], 'Tech': ['component/ devices/ build/ communication/ value/ enterprise/ technician/ skill/ data/ networks/ mobile/ design/ networking/ psychology/ productivity/ telephone/ primates/ gold/ silver']}, 20: {'World': ['discourse/ bloc/ expert/ city/ power/ negotiation/ rebellion/ property/ law/ manipulation/ judiciary/ clans/ administration/ ethics/ tribes/ communism/ democrat/ imperialism/ election/ anarchism'], 'Sports': ['event/ shot/ feature/ clubs/ shooter/ defense/ dexterity/ defence/ television/ recreational/ football/ models/ average/ esports/ youth/ soccer/ golf/ chess/ cricket/ wrestling'], 'Business': ['remainder/ oversees/ browse/ sector/ stock/ market/ dealer/ exchange/ broker/ capital/ money/ dealings/ resources/ consumer/ distribution/ communications/ forestry/ retail/ telecom/ traffic'], 'Tech': ['expand/ technical/ devices/ communication/ value/ enterprise/ technician/ skill/ data/ networks/ mobile/ networking/ psychology/ science/ productivity/ telephone/ mathematics/ primates/ gold/ silver']}}


        hypothesis_emo_synsand_LTOS ={2: {'World': ['expert and profit'], 'Sports': ['bob and football'], 'Business': ['capital and prehistoric'], 'Tech': ['developer and enterprise']}, 3: {'World': ['officer and federal and education'], 'Sports': ['competitions and wage and football'], 'Business': ['capital and communications and transportation'], 'Tech': ['computers and developer and gold']}, 4: {'World': ['officer and federal and education and anarchism'], 'Sports': ['competitions and wage and defense and average'], 'Business': ['stock and capital and communications and transportation'], 'Tech': ['enterprise and psychology and gold and robotics']}, 5: {'World': ['bloc and tribute and education and anarchism and minimalist'], 'Sports': ['competition and defense and recreational and model and average'], 'Business': ['stock and capital and money and store and economic'], 'Tech': ['enterprise and skill and biomedical and psychology and gold']}, 6: {'World': ['bloc and property and tribute and education and anarchism and minimalist'], 'Sports': ['sports and defense and football and puck and fun and golf'], 'Business': ['stock and capital and money and resources and consumer and communications'], 'Tech': ['specialized and solutions and developer and skill and productivity and gold']}, 7: {'World': ['bloc and negotiation and property and allegiance and curfew and tribute and anarchism'], 'Sports': ['competition and tournament and defense and defence and television and puck and wrestling'], 'Business': ['stock and capital and money and consumer and economic and communications and agriculture'], 'Tech': ['specialized and solutions and value and developer and skill and psychology and gold']}, 8: {'World': ['property and manipulation and petition and ethics and tribute and imperialism and education and anarchism'], 'Sports': ['tournament and season and defense and defence and puck and soccer and golf and wrestling'], 'Business': ['stock and broker and capital and money and resources and commission and consumer and communications'], 'Tech': ['specialized and communication and value and technician and skill and cryptography and primates and gold']}, 9: {'World': ['bloc and negotiation and property and allegiance and curfew and imperialism and socialist and conspiracy and anarchism'], 'Sports': ['competition and shot and season and defense and model and football and youth and puck and wrestling'], 'Business': ['stock and broker and capital and money and commission and consumer and communications and retail and tourism'], 'Tech': ['use and systems and technical and value and physic and skill and psychology and primates and gold']}, 10: {'World': ['officer and negotiation and federal and property and allegiance and petition and clans and democrat and anarchism and minimalist'], 'Sports': ['event and shot and season and defense and model and football and youth and puck and soccer and wrestling'], 'Business': ['stock and capital and resources and consumer and economic and communications and retailer and humanities and transportation and retail'], 'Tech': ['systems and transformer and value and developer and skill and networks and cryptography and primates and gold and silver']}, 11: {'World': ['negotiation and senator and federal and property and allegiance and clans and communism and democrat and imperialism and anarchism and minimalist'], 'Sports': ['event and competition and tournament and season and defense and television and football and youth and puck and cricket and wrestling'], 'Business': ['stock and market and dealer and broker and capital and money and commission and consumer and communications and retail and agricultural'], 'Tech': ['use and systems and technical and devices and transformer and value and skill and psychology and primates and gold and silver']}, 12: {'World': ['official and officer and federal and political and property and petition and curfew and ethics and tribes and democrat and imperialism and anarchism'], 'Sports': ['event and competition and tournament and season and defense and defence and television and football and average and youth and puck and wrestling'], 'Business': ['stock and dealer and purchase and broker and capital and money and consumer and economic and communications and labor and retail and agricultural'], 'Tech': ['use and systems and transformer and value and skill and data and networks and mobile and cryptography and primates and gold and silver']}, 13: {'World': ['official and expert and officer and rebellion and property and manipulation and petition and colonies and tribes and democrat and imperialism and anarchism and minimalist'], 'Sports': ['event and competition and shot and tournament and season and defense and defence and television and football and average and youth and puck and wrestling'], 'Business': ['stock and interchange and exchange and trades and broker and capital and money and consumer and economic and communications and services and retailer and agricultural'], 'Tech': ['systems and transformer and value and developer and strategy and skill and data and networks and productivity and cryptography and primates and gold and silver']}, 14: {'World': ['bloc and officer and negotiation and rebellion and property and company and petition and administration and curfew and ethics and tribes and democrat and imperialism and anarchism'], 'Sports': ['event and competition and shot and tournament and season and defense and defence and television and football and average and youth and puck and cricket and wrestling'], 'Business': ['bureau and stock and trades and capital and money and wholesale and commission and local and communications and retailer and retail and shopping and tourism and agricultural'], 'Tech': ['use and systems and devices and transformer and value and applications and skill and innovation and data and cryptography and telephone and primates and gold and silver']}, 15: {'World': ['bloc and power and negotiation and property and allegiance and manipulation and clans and administration and tribes and communism and democrat and imperialism and election and anarchism and minimalist'], 'Sports': ['event and competition and shot and feature and boast and defense and defence and television and football and average and youth and puck and chess and cricket and wrestling'], 'Business': ['bureau and stock and dealer and exchange and capital and money and dealings and shop and consumer and communications and services and retailer and forestry and antique and tourism'], 'Tech': ['use and technical and devices and communication and value and enterprise and skill and data and networking and productivity and cryptography and telephone and primates and gold and silver']}, 16: {'World': ['bloc and expert and power and federation and negotiation and federal and rebellion and property and administration and legislation and tribes and communism and democrat and imperialism and anarchism and corruption'], 'Sports': ['event and competition and shot and feature and season and boast and defense and defence and television and football and average and youth and hockey and cricket and volleyball and wrestling'], 'Business': ['bureau and department and stock and committee and interchange and trades and capital and money and trader and consumer and commodity and economic and retail and traffic and tourism and agricultural'], 'Tech': ['component and use and devices and solutions and value and enterprise and technician and skill and data and networking and productivity and cryptography and telephone and primates and gold and silver']}, 17: {'World': ['bloc and expert and power and federation and negotiation and coalition and federal and rebellion and property and clans and administration and ideology and tribes and communism and democrat and imperialism and anarchism'], 'Sports': ['event and competition and bout and shot and feature and boast and shooter and defense and defence and television and football and average and youth and hockey and chess and cricket and wrestling'], 'Business': ['stock and committee and exchange and purchase and broker and capital and money and dealings and payment and export and trader and resources and consumer and communications and vice and retail and traffic'], 'Tech': ['systems and devices and transformer and complicate and value and skill and innovation and data and mobile and science and productivity and cryptography and telephone and primates and gold and silver and physics']}, 18: {'World': ['expert and negotiation and senator and coalition and federal and rebellion and property and law and clans and administration and legislation and curfew and tribes and communism and democrat and imperialism and anarchism and minimalist'], 'Sports': ['event and shot and feature and professional and clubs and boast and shooter and defense and dexterity and defence and television and recreational and football and average and youth and chess and cricket and wrestling'], 'Business': ['remainder and bureau and stock and exchange and purchase and secretary and capital and money and resources and sell and economic and communications and services and merchants and labor and antique and shopping and agricultural'], 'Tech': ['systems and devices and transformation and value and physic and skill and innovation and data and club and mobile and weapon and design and psychology and productivity and telephone and primates and gold and silver']}, 19: {'World': ['country and officer and coalition and federal and property and mislead and allegiance and petition and clans and administration and curfew and ethics and tribes and democrat and imperialism and bureaucracy and socialist and education and anarchism'], 'Sports': ['event and shot and feature and clubs and boast and defense and dexterity and defence and television and football and average and youth and soccer and hockey and chess and surf and cricket and volleyball and wrestling'], 'Business': ['bureau and browse and stock and buyer and purchase and trades and capital and money and resources and commission and sell and commerce and entrepreneurship and merchandise and evasion and forestry and retail and antique and traffic'], 'Tech': ['component and devices and build and communication and value and enterprise and technician and skill and data and networks and mobile and design and networking and psychology and productivity and telephone and primates and gold and silver']}, 20: {'World': ['discourse and bloc and expert and city and power and negotiation and rebellion and property and law and manipulation and judiciary and clans and administration and ethics and tribes and communism and democrat and imperialism and election and anarchism'], 'Sports': ['event and shot and feature and clubs and shooter and defense and dexterity and defence and television and recreational and football and models and average and esports and youth and soccer and golf and chess and cricket and wrestling'], 'Business': ['remainder and oversees and browse and sector and stock and market and dealer and exchange and broker and capital and money and dealings and resources and consumer and distribution and communications and forestry and retail and telecom and traffic'], 'Tech': ['expand and technical and devices and communication and value and enterprise and technician and skill and data and networks and mobile and networking and psychology and science and productivity and telephone and mathematics and primates and gold and silver']}}

    spromt = ['syns', 'synspace', 'synslash', 'synsand']
    n_clusternum = arange(2, 21)
    for dataname in datasetnames:
        hypothesis = f'template/template_{dataname.lower()}.csv'
        for td in traindev:
            for sprompt in spromt:
                for num in n_clusternum:
                    print(f'{dataname}  {td} {sprompt} {num}\n')
                    if td == 'test':
                        savefile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + 'entail.csv'
                        modifiedfile = f'./embed/entail/{k}/' + dataname.lower() + '_' + str(num) +  '_' + sprompt + '_' + td + '.csv'
                        train = '32-shot-dataset/agnews/'+ dataname.lower() + '_test.csv'
                        rows = []
                        with open(train) as f:
                            csv_read = csv.reader(f)
                            for row in csv_read:
                                label =  [
                                            'World',
                                            'Sports',
                                            'Business',
                                            'Tech']
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

                            train =  '32-shot-dataset/agnews/' + dataname.lower() + '_select_' + td + '_' + str(n) + '.csv'
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
                                            label =  [
                                            'World',
                                            'Sports',
                                            'Business',
                                            'Tech']
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
        maintrec(k)
        mainsst2(k)
        maincr(k)
        mainagnews(k)
