from Classes import TankTree
import os
from Base.query import ExistForId, IfList
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Ввод не может быть пустым или состоять только из пробелов. Пожалуйста, попробуйте снова.")
def get_valid_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            num = int(user_input)
            if num >= 0:
                return num
        print("Пожалуйста, введите корректное положительное целое число.")

tree = TankTree()
while True:
        print("0. Вывод всего дерева")
        print("1. Добавить лист")
        print("2. Удалить лист по ID")
        print("3. Удалить поддерево по ID родителя")
        print("4. Удалить узел без поддерева по ID узла")
        print("5. Получить прямых детей по ID родителя")
        print("6. Получить прямого родителя по ID узла")
        print("7. Получить всех потомков по ID узла")
        print("8. Получить всех предков по ID узла")
        print("9. Выход")

        choice = get_valid_int("Выберите действие: ")
        os.system('cls')
        if choice == 0:
            node_id = 1
            descendants = tree.get_all_descendants(node_id)
            result = tree.get_element(node_id)
            print (f"Исходный узел: {result}")
            print("Все потомки:")
            for descendant, level in descendants:
                print(f"'{descendant[0]}'" + " " * (
                            level * 4) + f"'{descendant[2]}'")
        if choice == 1:
            parent_id = get_valid_int("Введите ID родителя: ")
            if(ExistForId(parent_id)):
                name = get_valid_input("Введите имя название танка: ")
                tree.add_leaf(parent_id, name)
                print("Танк добавлен.")
            else:
                print("Нет такого родителя")
            
        elif choice == 2:
            leaf_id = get_valid_int("Введите ID узла для удаления: ")
            if (IfList(leaf_id)):
                tree.delete_leaf(leaf_id)
            else:
                print("Не лист дерева")
        elif choice == 3:
            parent_id = get_valid_int("Введите ID родителя для удаления поддерева: ")
            tree.delete_subtree(parent_id)
            
        elif choice == 4:
            leaf_id = get_valid_int("Введите ID узла для удаления: ")
            tree.delete_node_with_subtree(leaf_id)
             
        elif choice == 5:
            parent_id = get_valid_int("Введите ID родителя для получения детей: ")
            children = tree.get_direct_children(parent_id)
            print("Прямые дети:")
            for child in children:
                print(f"'{child[0]}', '{child[2]}'")

        elif choice == 6:
            node_id = get_valid_int("Введите ID узла для получения родителя: ")
            parent = tree.get_direct_parent(node_id)
            print("Прямой родитель:", parent)

        elif choice == 7:
            node_id = get_valid_int("Введите ID узла для получения потомков: ")
            descendants = tree.get_all_descendants(node_id)
            result = tree.get_element(node_id)
            print (f"Исходный узел: {result}")
            print("Все потомки:")
            for descendant, level in descendants:
                print(f"'{descendant[0]}'" + " " * (
                            level * 4) + f"'{descendant[2]}'")
            
        elif choice == 8:
            node_id = get_valid_int("Введите ID узла для получения предков: ")
            ancestors = tree.get_all_ancestors(node_id)
            result = tree.get_element(node_id)
            print(f"Исходный узел: {result}")
            print("Все предки:")
            for ancestor, level in ancestors:
                print(f"'{ancestor[0]}'" + " " * (abs(level) * 4) + f"'{ancestor[2]}'")

        elif choice == 9:
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


tree.close()