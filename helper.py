def add_subtopic(parent, node):
    sub_topic = parent.addSubTopic()
    sub_topic.setTitle(node["title"])
    if "children" in node:
        for each_child in node["children"]:
            add_subtopic(sub_topic, each_child)


def generate_markdown(node, level=1):
    if "children" in node:
        markdown_str = (level + 1) * "#" + " " + node["title"] + "\n"
        for each_child in node["children"]:
            markdown_str += generate_markdown(markdown_str, each_child, level + 1)
    else:
        markdown_str = node["title"] + "\n\n"
    return markdown_str
