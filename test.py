from sklearn.feature_extraction.text import TfidfTransformer

  csv_dir = dir + yyyy + '_' + mm  
  csv_list = os.listdir(csv_dir)
  csv_list.sort()
  week_num = 1
  for i in csv_list:
    tmp_pd = pd.read_csv(csv_dir + '/' + i, index_col = 0) # 한 주의 DTM 파일을 읽어옴
    tmp_pd.pop(tmp_pd.columns[0])

    # 사이킷런을 이용하여 TFIDF 생성
    tfidf = TfidfTransformer().fit_transform(tmp_pd)
    tfidf_array = tfidf.toarray()
    tfidf_data_frame = pd.DataFrame(tfidf_array, columns = tmp_pd.columns)
    
    # 1. TF-IDF RANK 구하기
    rank_df = pd.DataFrame()

    for index in range(len(tfidf_data_frame)):
      df1 = tfidf_data_frame[index:index+1].T     
      df1_sort = df1.sort_values(by = index,ascending=False) # tf-idf값 높은 순서대로 정렬
      df1_high = df1_sort.head(30)
      df_rank =df1_high.rank(method='first', ascending=False) # 순위 매김 
      df2 = df_rank.T  
      rank_df = rank_df.append(df2) 

    rank_df = rank_df.fillna(0) # NaN값 처리
    
    # 2. TF-IDF 표준편차 구하기
    sample_df = pd.DataFrame()
    
    # 2) 키워드의 표준편차 구하기 
    rank_var = np.var(rank_df)
    rank_22=  rank_var.sort_values(ascending=False) # 높은 순서대로 표준편차
    rank_true = (rank_22 >=1) # 표준편차 1 이상인 키워드 = True

    stop_keyword = []
    num = 0 
  # 표준편차 1 넘지 못하는 단어들 --> 불용어 수준의 단어들 = stop_keyword
    for i in range(len(rank_true)):
      if(rank_true[i] == False):  # 표준편차 1 이하인 단어들 = False
        num = num + 1 ##
        rank_true.index[i]
        # 불용어 수준의 단어들
        stop_keyword.append(rank_true.index[i]) # stop_keyword들임 
    sample_df=rank_df

    # 불용어 수준의 단어들 제거 - stop_keyword
    for j in range(len(rank_df.columns)):
      for stop_key in stop_keyword:
        if(rank_df.columns[j]==stop_key):
          sample_df = sample_df.drop([rank_df.columns[j],],axis=1)
    
    
    # --------------------------
    
import os
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

gisa_df = pd.DataFrame()
csv_dir = dir + yyyy + '_' + mm 
csv_list = os.listdir(csv_dir)
csv_list.sort()

for i in csv_list:
    tmp_pd = pd.read_csv(csv_dir + '/' + i, index_col = 0) # 한 주의 DTM 파일을 읽어옴
    gisa_df = gisa_df.append(tmp_pd) 

gisa_df = gisa_df.fillna(0)
gisa_df[gisa_df < 0] = False 
gisa_df[gisa_df >=1] = True

frequent = apriori(gisa_df, min_support = 0.01, use_colnames = True) 
final_frequent_2 = pd.DataFrame()

for x, y, z in zip(range(len(frequent)), list(frequent['itemsets']), frequent['support']):
  if(len(y) == 2) : 
    line = {'support' : z, 'itemsets' : y}
    final_frequent_2 = final_frequent_2.append(line, ignore_index=True)
      
      #----------------
      
 title.reset_index(drop=True, inplace=True)
  link.reset_index(drop=True, inplace=True)
  content.reset_index(drop=True, inplace=True)

  # 노드의 내용을 읽고 [기사 내용]에서 그 노드 값이 들어간 기사를 찾아서
  # [기사 제목]과 [기사 링크]를 hover로 둔다.

  output_notebook()

  HOVER_TOOLTIPS = [            
      ("키워드", "@index"),
      ("연관 단어 수", "@degree"),
      ("관련 기사 제목", "@title"),
      ("관련 기사 링크", "@link")
  ]

  # 기본 bokeh 플랏 구성
  plot = figure(tooltips = HOVER_TOOLTIPS, plot_width=1000, plot_height=1000, # 800 800
              x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), tools="pan, tap, wheel_zoom, save, reset",
                active_scroll='wheel_zoom')

  plot.title.text = yyyy + "년 " + mm + "월 뉴스 시각화 그래프"


  ## openUrl 기능..##
  ##### 노드마다 속성 추가하고 hover tool tip에서 자동으로 tap 가능해야 함!!####
  # @ 으로 속성 접근 가능

  url = '@link'
  taptool = plot.select(type=TapTool) ##########################################################################################################################################################################################여기
  taptool.callback = OpenURL(url=url)


  #content = urlopen(link).read()

  # 각 노드의 차수 계산하고 노드 속성에 추가
  degrees = dict(nx.degree(G))
  degrees2 = [0 * val for (node, val) in G.degree()]
  nx.set_node_attributes(G, name='degree', values=degrees)

  # 노드에 기사 링크 속성 추가
  link_set = []
  title_set = []
  for i in G.nodes():
    link_sheet = []
    word = i[1:-1]
    for j, k in zip(content, range(len(content))):
      if j.find(word) > 0:
        link_sheet.append(k)
    num = random.choice(link_sheet)
    link_set.append(link[num])
    title_set.append(title[num])
  link_dictionary = dict(zip(G.nodes(), link_set))
  title_dictionary = dict(zip(G.nodes(), title_set))
  nx.set_node_attributes(G, name='link', values=link_dictionary)
  nx.set_node_attributes(G, name='title', values=title_dictionary)
