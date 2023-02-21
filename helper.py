def add_subtopic(parent, node):
    sub_topic = parent.addSubTopic()
    try:
        sub_topic.setTitle(node["title"])
    except TypeError:
        sub_topic.setTitle(node)
    if "children" in node:
        for each_child in node["children"]:
            add_subtopic(sub_topic, each_child)


def generate_markdown(node, level=2):
    if "children" in node:
        if level < 7:
            markdown_str = level * "#" + " " + node["title"] + "\n"
        else:
            markdown_str = (level - 7) * "  " + " - " + node["title"] + "\n"
        for each_child in node["children"]:
            markdown_str += generate_markdown(each_child, level + 1)
    else:
        try:
            markdown_str = node["title"] + "\n\n" if level < 7 else (level - 7) * "  " + " - " + node["title"] + "\n"
        except TypeError:
            markdown_str = node + "\n\n" if level < 7 else (level - 7) * "  " + " - " + node + "\n"
    return markdown_str
