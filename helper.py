def add_subtopic(parent, node):
    sub_topic = parent.addSubTopic()
    sub_topic.setTitle(node["title"] if type(node) == dict else node)
    if "children" in node:
        for each_child in node["children"]:
            add_subtopic(sub_topic, each_child)


def generate_markdown(node, level=2):
    if "children" in node:
        markdown_str = (level * "#" + " " if level < 7 else (level - 7) * "  " + " - ") + node["title"] + "\n"
        for each_child in node["children"]:
            markdown_str += generate_markdown(each_child, level + 1)
    else:
        content = node["title"] if type(node) == dict else node
        markdown_str = content + "\n\n" if level < 7 else (level - 7) * "  " + " - " + content + "\n"
    return markdown_str
