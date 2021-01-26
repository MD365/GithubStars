import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python'
r = requests.get(url)
print("status code :",r.status_code)

#将响应存储在一个变量中
response_dict = r.json()
print("total repostiories",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar( my_config,style=my_style)
chart.title = 'Most-Starred python projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python.repos.svg')








# print("repostiories returned", len(repo_dicts))
#
# print("\n Selected information about ech repository:")
# #研究第一个仓库
# # repo_dict = repo_dicts[0]
# for repo_dict in repo_dicts:
#     print("\n selected information about first repostitory:")
#     print('name:',repo_dict['name'])
#     print('owner:',repo_dict['owner']['login'])
#     print('stars',repo_dict['stargazers_count'])
#     print('repository:',repo_dict['html_url'])
#     print('create:',repo_dict['created_at'])
#     print('updated:',repo_dict['updated_at'])
#     print('description:',repo_dict['description'])
#
# # print("\n",repo_dict)
# # for key in sorted(repo_dict.keys()):
# #     print(key)
