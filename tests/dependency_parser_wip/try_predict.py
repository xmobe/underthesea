from underthesea.models.dependency_parser import DependencyParser

parser = DependencyParser.load('tmp/resources/parsers/vi-dp-v1a0')
dataset = parser.predict(
    [['Đó', 'là', 'kết quả', 'của', 'cuộc', 'vật lộn', 'bền bỉ', 'gần', '17', 'năm', 'của', 'Huỳnh Đỗi', '.']],
    verbose=False)
print(dataset.sentences)
