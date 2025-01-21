#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
import streamlit as st 
import numpy as np
import pandas as pd
import pickle

st.title("PRESS RELEASE")
st.subheader("Deep Learning - AI Model")
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    df = pd.read_csv("",usecols=["Title","Description","Scrapped_text"])
else:
    print("File not found")


data_load_state = st.text("Loading Data....")

if st.button("Download Results"):
    pickled_model = pickle.load(open("pr.pkl",'rb'))
    data = st.dataframe(df)
    data = st.load_data(df.shape[0])
    data= df.loc[['Title','Description','Scrapped']].reshape(1,-1)
    data_load_state.text("Loading Data.... Done!")
        
    result = pickled_model.predict(data)[0]
    data_load_state.text("Predicting.....")
    if result ==0 :
        st.write(f"### Press Release Category : **E-Commerce**",unsafe_allow_html = True)
    elif result ==1 :
        st.write(f"### Press Release Category : **Financial Services**",unsafe_allow_html = True)
    elif result ==2 :
        st.write(f"### Press Release Category : **Media**",unsafe_allow_html = True)
    elif result ==3 :
        st.write(f"### Press Release Category : **Health**",unsafe_allow_html = True)
    elif result ==4 :
        st.write(f"### Press Release Category : **Technology**",unsafe_allow_html = True)
    elif result ==5 :
        st.write(f"### Press Release Category : **Insurance**",unsafe_allow_html = True)
    elif result ==6 :
        st.write(f"### Press Release Category : **Hospitality**",unsafe_allow_html = True)
    elif result ==7 :
        st.write(f"### Press Release Category : **Manufacturing**",unsafe_allow_html = True)
    elif result ==8 :
        st.write(f"### Press Release Category : **Transport & Logistics**",unsafe_allow_html = True)

    else :
        st.write(f"### Press Release Category : **Tourism**",unsafe_allow_html = True)
  """  


# In[ ]:


import streamlit as st 
import numpy as np
import pandas as pd
import pickle
import time
import numpy as np
import pandas as pd
import seaborn as sns
import concurrent.futures
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import classification_report,confusion_matrix
# from sklearn.model_selection import train_test_split
import os
import re
import string
# from spacy.lang.en.stop_words import STOP_WORDS
# from sklearn.svm import SVC
from datetime import date
import os
import requests 
import os.path
import re
from bs4 import BeautifulSoup

from googletrans import Translator
import requests 
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer(r'sentence_transformer\all-MiniLM-L6-v2')

# import plotly.figure_factory as ff
st.set_option('deprecation.showPyplotGlobalUse', False)
# st.image("nttlogo-blue.png",width=250,use_cloumn_width=2200,clamp=True)
st.image("nttlogo-blue.png", caption=None, width=250, use_column_width=2200, clamp=False, channels="RGB", output_format="auto")

activities = ["Classifier"]
st.sidebar.header("DEEP LEARNING AI APPLICATION")
st.sidebar.image("5396346-removebg-preview.png")
choice = st.sidebar.selectbox("Select Activities",activities)
st.sidebar.header("About")
st.sidebar.write("An internal tool for classifying the news articles to their respective domains. It scans the articles and utilize Deep Learning technology to categorize them.")
#translating to eng , classifying  doamin
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("© 2022 NTT DATA, Inc. All rights reserved.")

if choice == 'Classifier':
    html_temp = """
    
    <h1 style="color:white;width:100;height:500;text-align:left;">PRESS RELEASE CLASSIFIER</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write("AI-powered classifying tool will save your time. Simply upload the data below, and our AI will work with you to categorize your news articles to its respective domain.")
    #st.write("Use charts in power point presentations and in our websites.")

    

# def get_file(*paths):
#     path = os.path.join(*paths)
# try:
#     with open(path, 'rb') as f:
#         return f.read().decode('utf8')
# except IOError:
#     pass


# def get_version():
#     init_py = get_file(os.path.dirname(__file__), 'googletrans', '__init__.py')
#     pattern = r"{0}\W*=\W*'([^']+)'".format('__version__')
#     version, = re.findall(pattern, init_py)
#     return version


# def get_description():
#     init_py = get_file(os.path.dirname(__file__), 'googletrans', '__init__.py')
#     pattern = r'"""(.*?)"""'
#     description, = re.findall(pattern, init_py, re.DOTALL)
#     return description


# def get_readme():
#     return get_file(os.path.dirname(__file__), 'README.rst')


# def install():
#     setup(
#         name='googletrans',
#         version=get_version(),
#         description=get_description(),
#         long_description=get_readme(),
#         license='MIT',
#         author='SuHun Han',
#         author_email='ssut' '@' 'ssut.me',
#         url='https://github.com/ssut/py-googletrans',
#         classifiers=['Development Status :: 5 - Production/Stable',
#                      'Intended Audience :: Education',
#                      'Intended Audience :: End Users/Desktop',
#                      'License :: Freeware',
#                      'Operating System :: POSIX',
#                      'Operating System :: Microsoft :: Windows',
#                      'Operating System :: MacOS :: MacOS X',
#                      'Topic :: Education',
#                      'Programming Language :: Python',
#                      'Programming Language :: Python :: 3.6',
#                      'Programming Language :: Python :: 3.7',
#                      'Programming Language :: Python :: 3.8'],
#         packages=find_packages(exclude=['docs', 'tests']),
#         keywords='google translate translator',
#         install_requires=[
#             'httpx==0.13.3',
#         ],
#         python_requires= '>=3.6',
#         tests_require=[
#             'pytest',
#             'coveralls',
#         ],
#         scripts=['translate']
#     )

    translator = Translator()

        

    
    # st.title("PRESS RELEASE CLASSIFIER")
    # st.subheader("Deep Learning - AI Application")
    uploaded_file = st.file_uploader("")


    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # st.dataframe(df.head())
    else:
        print("File not found")



    if uploaded_file and df is not None:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.001)
            my_bar.progress(percent_complete + 1)


    ####################################################################################################################
    if st.button("Predict"):
        if uploaded_file and df is not None:


            # # Scanned all articles. 
            # """

            st.write('*Scanned all articles* :sunglasses:')

        # getting non article data
            df_ne = df[df["Language"] != "English"].reset_index(drop = True).copy()
            df_e = df[df["Language"] == "English"].reset_index(drop = True).copy()


        ### Web Scrapping - getting the content from url
            def get_content(url):
                try:
            #         del wiki_text
                    req_obj = requests.get(url)
                    text = req_obj.text
                    soup = BeautifulSoup(text)
                    all_paras = soup.find_all("p")
                    wiki_text = ''
                    for para in all_paras:
                        wiki_text += para.text 

                    return wiki_text

                except:
                    pass
            with concurrent.futures.ThreadPoolExecutor(max_workers=14) as excecutor:
                results = [excecutor.submit(get_content, url) for url in df_ne["URL"]]
                output = [out.result() for out in concurrent.futures.as_completed(results)]

            df_ne["Sentence"] = output

            ### DATA TRANSLATION
            def get_Translate(text):
                translation = translator.translate(text,dest='en')
                return translation.text

            df_ne["Translated_eng"] = df_ne["Sentence"].apply(lambda text:get_Translate(text))

            ### PREPARE DATA
            df_e["Translated_eng"] = df_e["Title / Contents"] + " " + df_e["Description"]
            df_new = pd.concat([df_e,df_ne], axis = 0).reset_index(drop=True)


            ### MODEL PORTION
            domain_list = ["Manufacturing", "Retail", "Health", "Insurance", 
                   "Financial Service", "Technology", "Energy",
                  "Transport And Logistics", "Telecom", "Media", "Hospitality and Tourism",
                   "Automobile", "Infrastructure", "Real estate","Defence","Government",
                  ]

            tensor_list = []
            for i,k in enumerate(domain_list): 
                tensor = model.encode(domain_list[i],convert_to_tensor=True)
                tensor_list.append(tensor)


            label_data = pd.DataFrame()
            label_data["Domain"] = domain_list
            label_data["Domain_embed"] = tensor_list


            def DomainClassifier(sen):
                sen_embed = model.encode(sen[0], convert_to_tensor=True)

                domain_names = []
                domain_scores = []

                for i,k in zip(label_data["Domain"], label_data["Domain_embed"]):
                    score = util.pytorch_cos_sim(sen_embed, k)
                    domain_names.append(i)
                    domain_scores.append(score)

                score_data = pd.DataFrame()
                score_data["Domain"] = domain_names
                score_data["Score"] = np.array(domain_scores,dtype=object)
                score_data.sort_values(by = "Score", ascending = False, inplace=True)
                score_data.reset_index(drop = True, inplace = True)
                return list(score_data["Domain"].head(3))



            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as excecutor:
                results = [excecutor.submit(DomainClassifier, [sen]) for sen in df_new["Translated_eng"]]
                output = [out.result() for out in concurrent.futures.as_completed(results)]
            df_new["Domain_Pred"] = output

    #         ### TFIDF PORTION

    #         filename = 'tfidf.pkl'
    #         with open(filename, 'rb') as file: 
    #             cv = pickle.load(file)

    #         vectors = cv.transform(df['TITLE_DESC'])

    #         ### Encode Portion
    #         filename = 'encode.pkl'
    #         with open(filename, 'rb') as file:
    #             encode = pickle.load(file)

    #         ### CONFIDENCE SCORE PART PORTION

    #         n_classes = 7
    #         n_samples = df.shape[0]

    #         prob_pred = np.zeros((n_samples, n_classes))
    #         class_pred = np.zeros(n_samples)

    #         classes = [0, 1, 2, 3, 4, 5, 6]

    #         for c in classes:
    #             print(c)


    #             filename = f"classifier_{c}.pkl"
    #             with open(filename, 'rb') as file:
    #                 model = pickle.load(file)

    #             prob_pred[:, c] = model.predict_proba(vectors)[:, 1]

    #         prob_pred /= prob_pred.sum(axis=1).reshape((prob_pred.shape[0], -1))

    #         classes_names = encode.inverse_transform(classes)
    #         pred_df = pd.DataFrame(prob_pred, columns=classes_names)
    #         pred_df = pred_df*100
    #         pred_df['arg'] = pred_df.values.argmax(axis=1)
    #         pred_df['Max_value'] = [pred_df.iloc[n,i] for n,i in enumerate(pred_df['arg'])]


    #         thresh = 60
    #         pred_df['Confidence_Level'] = 'Low'
    #         pred_df.loc[(pred_df['Max_value']>=thresh) , 'Confidence_Level'] = 'High'


    #         final_df = pd.concat([df.reset_index(drop = True), pred_df.reset_index(drop = True)], axis = 1)

    #         #Model Portion

    #         filename = "ovr_model.pkl"
    #         with open(filename, 'rb') as file:
    #             ovr_model = pickle.load(file)

    #         ovr_pred = ovr_model.predict(vectors)
    #         final_df["Prediction"] = encode.inverse_transform(ovr_pred)
    #         final_df = final_df.drop(["Title / Contents1","Description1", "arg", "Max_value"], axis = 1)


    #         def get_possiblecat(x):
    #             lis = final_df[["AR Report / Market Insight","Award/Contest Winner","Business Partnership",
    #          "Corporate Information",
    #               "Merger & Acquisition","Offering","Won Project"]].T[x].sort_values(ascending=False)[:3].index
    #             return list(lis)

    #         final_df.reset_index(inplace = True)
    #         final_df["Possible Categories"] = final_df["index"].apply(lambda x:get_possiblecat(x))

    #         final_df.loc[final_df["Confidence_Level"]=="High", "Possible Categories"] = "Not Applicable" 

    #         #POST MODEL

    #         def overall(x):
    #     #     res1 = re.findall("survey",str(x).lower())
    #             res2 = re.findall("award",str(x).lower())
    #             res3 = re.findall("acquire",str(x).lower())
    #             res4 = re.findall("recogn",str(x).lower())
    #         #     if "survey" in res1:
    #         #         return 'AR Report / Market Insight'
    #             if "award" in res2:
    #                 return 'Award/Contest Winner'
    #             if "acquire" in res3:
    #                 return 'Merger & Acquisition'
    #             if "acquire" in res4:
    #                 return 'Award/Contest Winner'
    #             else:
    #                 return 'null'

    #         final_df['pred1'] = 'null'
    #         final_df['pred1'] = final_df['TITLE_DESC'].apply(lambda x: overall(x))

    #         final_df.loc[final_df['pred1']=='null','pred1'] = final_df[final_df['pred1']=='null']['Prediction']

    #         final_df_data = final_df.drop(['TITLE_DESC', "AR Report / Market Insight","Award/Contest Winner","Business Partnership",
    #          "Corporate Information", "Prediction",
    #               "Merger & Acquisition","Offering","Won Project"], axis = 1) 
    #         final_df_data['Prediction'] = final_df_data['pred1']
    #         final_df_data = final_df_data[["Title / Contents", "Description","URL","Prediction", "Confidence_Level", "Possible Categories"]]


    #         # st.dataframe(final_df_data.sample(10))


            ###Downloading Sections

            today = date.today()
            # print("Today's date:", today)
            # Month abbreviation, day and year	
            date_today = today.strftime("%b-%d-%Y")
            # print("d4 =", d4)

            @st.cache
            def convert_df(dataframe):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return dataframe.to_csv(index = False).encode('utf-8')

            csv = convert_df(df_new)

            st.download_button(
                label="Export",
                data=csv,
                file_name='result_' + date_today + '.csv',
                mime='text/csv',
            )

            del df_new














    # st.expander("See explanation")

    # with st.expander("See explanation"):
    #     st.write("""
    #         The chart above shows some numbers I picked for you.
    #         I rolled actual dice for these, so they're *guaranteed* to
    #         be random.
    #     """)
    #     st.image("https://static.streamlit.io/examples/dice.jpg")


    # with st.container():
    #    st.write("This is inside the container")


    # # data_load_state = st.text("Loading Data....")

    # if st.button("Download Results"):
    #     pickled_model = pickle.load(open("pr.pkl",'rb'))
    #     data = st.dataframe(df)
    #     data = st.load_data(df.shape[0])
    #     data= df.loc[['Title','Description','Scrapped']].reshape(1,-1)
    #     data_load_state.text("Loading Data.... Done!")
            
    #     result = pickled_model.predict(data)[0] 
    #     data_load_state.text("Predicting.....")
    #     if result ==0 :
    #         st.write(f"### Press Release Category : **AR Reports & Market Insights**",unsafe_allow_html = True)
    #     elif result ==1 :
    #         st.write(f"### Press Release Category : **Award**",unsafe_allow_html = True)
    #     elif result ==2 :
    #         st.write(f"### Press Release Category : **Business Partnership**",unsafe_allow_html = True)
    #     elif result ==3 :
    #         st.write(f"### Press Release Category : **Corporate Information**",unsafe_allow_html = True)
    #     elif result ==4 :
    #         st.write(f"### Press Release Category : **Mergers & Accqusitions**",unsafe_allow_html = True)
    #     elif result ==5 :
    #         st.write(f"### Press Release Category : **Offerings**",unsafe_allow_html = True)
    #     else :
    #         st.write(f"### Press Release Category : **Won Project**",unsafe_allow_html = True)
    
#         if result ==0 :
#         st.write(f"### Press Release Category : **E-Commerce**",unsafe_allow_html = True)
#     elif result ==1 :
#         st.write(f"### Press Release Category : **Financial Services**",unsafe_allow_html = True)
#     elif result ==2 :
#         st.write(f"### Press Release Category : **Media**",unsafe_allow_html = True)
#     elif result ==3 :
#         st.write(f"### Press Release Category : **Health**",unsafe_allow_html = True)
#     elif result ==4 :
#         st.write(f"### Press Release Category : **Technology**",unsafe_allow_html = True)
#     elif result ==5 :
#         st.write(f"### Press Release Category : **Insurance**",unsafe_allow_html = True)
#     elif result ==6 :
#         st.write(f"### Press Release Category : **Hospitality**",unsafe_allow_html = True)
#     elif result ==7 :
#         st.write(f"### Press Release Category : **Manufacturing**",unsafe_allow_html = True)
#     elif result ==8 :
#         st.write(f"### Press Release Category : **Transport & Logistics**",unsafe_allow_html = True)

#     else :
#         st.write(f"### Press Release Category : **Tourism**",unsafe_allow_html = True)
        

