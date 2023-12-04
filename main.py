import requests
import json


def get_page(page_id):
	url_link_pre = "https://el.wikipedia.org/w/api.php?action=parse&format=json&pageid="
	url_link_meta = "&formatversion=2"
	req = requests.get(
	url_link_pre + str(page_id) + url_link_meta
	)
	return req


def valid_pages(limit_pages):
    valid = []
    for i in range(1, limit_pages):
        print(i)
        r_page = get_page(i)
        if "error" not in r_page.json():
            valid.append(i)

    return valid


def access_pages(list_page_id, dct, lst, node_list):
    
    for i in list_page_id:
        save_page(i, dct, lst, node_list)
    

def save_page(page_id, dct, lst, node_list):

    cont = (get_page(page_id).json())

    curr_title = cont["parse"]["title"]
    curr_links = cont["parse"]["links"]
    
    if curr_title not in titles_dict:
        titles_dict[curr_title] = len(titles_lst)
        titles_lst.append(curr_title)

    for link in curr_links:
        if link["exists"] == True:
            if link["title"] not in titles_lst:
                titles_dict[link["title"]] = len(titles_lst)
                titles_lst.append(link["title"])
            nodes.append((titles_dict[curr_title], titles_dict[link["title"]]))

titles_dict = {}
titles_lst = []
nodes = []

save_page(25, titles_dict, titles_lst, nodes)

print(titles_dict)
print(titles_lst)
print(nodes)


