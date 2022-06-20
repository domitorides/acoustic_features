import matplotlib.pyplot as plt

y_lfcc_decision_tree = [68, 59, 62, 56, 72]
y_mfcc_decision_tree = [74, 76, 76, 71, 74]
y_plp_decision_tree = [77, 80, 77, 77, 77]
y_spec_cent_decision_tree = [58, 60, 58, 64, 62]

y_lfcc_random_forest = [72, 68, 61, 68, 70]
y_mfcc_random_forest = [82, 86, 87, 84, 83]
y_plp_random_forest = [80, 76, 73, 79, 73]
y_spec_cent_random_forest = [70, 76, 71, 77, 78]


def decision_tree_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='Decision Tree results')

    # Графики по классификатору decision tree
    plt.plot(X, y_lfcc_decision_tree, 'r', label="LFCC")
    plt.plot(X, y_mfcc_decision_tree, 'g', label="MFCC")
    plt.plot(X, y_plp_decision_tree, 'b', label="PLP")
    plt.plot(X, y_spec_cent_decision_tree, 'm', label="SPECTRAL CENTROID")
    plt.legend()
    plt.xticks([])
    plt.title("Decision Tree results", fontsize=15)
    # plt.show()
    plt.savefig("Decision Tree results.png")


def decision_tree_result_bar_chart():
    X = 0.5
    width = 0.5

    # Гистограмма по классификатору decision tree
    fig, ax = plt.subplots(figsize=(12, 7), label='Decision Tree bar graph results')
    ax.bar(X, sum(y_spec_cent_decision_tree) / 5, width, label='SPECTRAL CENTROID')
    ax.bar(X + width, sum(y_lfcc_decision_tree) / 5, width, label='LFCC')
    ax.bar(X + width * 2, sum(y_mfcc_decision_tree) / 5, width, label='MFCC')
    ax.bar(X + width * 3, sum(y_plp_decision_tree) / 5, width, label='PLP')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("Decision Tree bar graph results", fontsize=15)
    # plt.show()
    plt.savefig("Decision Tree bar graph results.png")


def random_forest_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='Random Forest results')

    # Графики по классификатору decision tree
    plt.plot(X, y_lfcc_random_forest, 'r', label="LFCC")
    plt.plot(X, y_mfcc_random_forest, 'g', label="MFCC")
    plt.plot(X, y_plp_random_forest, 'b', label="PLP")
    plt.plot(X, y_spec_cent_random_forest, 'm', label="SPECTRAL CENTROID")
    plt.legend()
    plt.xticks([])
    plt.title("Random Forest results", fontsize=15)
    # plt.show()
    plt.savefig("Random Forest results.png")


def random_forest_result_bar_chart():
    X = 0.5
    width = 0.5

    # Гистограмма по классификатору decision tree
    fig, ax = plt.subplots(figsize=(12, 7), label='Random Forest bar graph results')
    ax.bar(X + width, sum(y_spec_cent_random_forest) / 5, width, label='SPECTRAL CENTROID')
    ax.bar(X, sum(y_lfcc_random_forest) / 5, width, label='LFCC')
    ax.bar(X + width * 3, sum(y_mfcc_random_forest) / 5, width, label='MFCC')
    ax.bar(X + width * 2, sum(y_plp_random_forest) / 5, width, label='PLP')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("Random Forest bar graph results", fontsize=15)
    plt.savefig("Random Forest bar graph results.png")
    # plt.show()


print("1 - Bar chart results decision tree")
print("2 - Linear results decision tree")
print("3 - Bar chart results random forest")
print("4 - Linear results random forest")
choose = int(input("Enter choose: "))
if choose == 1:
    decision_tree_result_bar_chart()
elif choose == 2:
    decision_tree_result_linear()
elif choose == 3:
    random_forest_result_bar_chart()
elif choose == 4:
    random_forest_result_linear()