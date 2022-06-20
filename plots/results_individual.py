import matplotlib.pyplot as plt
y_lfcc_decision_tree = [68, 59, 62, 56, 72]
y_mfcc_decision_tree = [74, 76, 76, 71, 74]
y_plp_decision_tree = [77, 80, 77, 77, 77]
y_spec_cent_decision_tree = [58, 60, 58, 64, 62]

y_lfcc_random_forest = [72, 68, 61, 68, 70]
y_mfcc_random_forest = [82, 86, 87, 84, 83]
y_plp_random_forest = [80, 76, 73, 79, 73]
y_spec_cent_random_forest = [70, 76, 71, 77, 78]


def mfcc_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='MFCC results')

    # Графики по классификатору decision tree
    plt.plot(X, y_mfcc_decision_tree, 'r', label="MFCC DECISION TREE")
    plt.plot(X, y_mfcc_random_forest, 'g', label="MFCC RANDOM FOREST")
    plt.legend()
    plt.xticks([])
    plt.title("MFCC linear", fontsize=15)
    # plt.show()
    plt.savefig("MFCC linear.png")


def mfcc_bar_chart():
    X = 0.5
    width = 0.5

    # Гистограмма по классификатору decision tree
    fig, ax = plt.subplots(figsize=(12, 7), label='MFCC bar chart')
    ax.bar(X, sum(y_mfcc_decision_tree) / 5, width, label='MFCC DECISION TREE')
    ax.bar(X + width, sum(y_mfcc_random_forest) / 5, width, label='MFCC RANDOM FOREST')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("MFCC bar chart", fontsize=15)
    # plt.show()
    plt.savefig("MFCC bar chart.png")


def lfcc_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='LFCC results')

    # Графики по классификатору decision tree
    plt.plot(X, y_lfcc_decision_tree, 'r', label="LFCC DECISION TREE")
    plt.plot(X, y_lfcc_random_forest, 'g', label="LFCC RANDOM FOREST")
    plt.legend()
    plt.xticks([])
    plt.title("LFCC linear", fontsize=15)
    # plt.show()
    plt.savefig("LFCC linear.png")


def lfcc_bar_chart():
    X = 0.5
    width = 0.5

    # Гистограмма по классификатору decision tree
    fig, ax = plt.subplots(figsize=(12, 7), label='LFCC bar chart')
    ax.bar(X, sum(y_lfcc_decision_tree) / 5, width, label='LFCC DECISION TREE')
    ax.bar(X + width, sum(y_lfcc_random_forest) / 5, width, label='LFCC RANDOM FOREST')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("LFCC bar chart", fontsize=15)
    # plt.show()
    plt.savefig("LFCC bar chart.png")


def plp_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='PLP results')

    # Графики по классификатору decision tree
    plt.plot(X, y_plp_decision_tree, 'r', label="PLP DECISION TREE")
    plt.plot(X, y_plp_random_forest, 'g', label="PLP RANDOM FOREST")
    plt.legend()
    plt.xticks([])
    plt.title("PLP linear", fontsize=15)
    # plt.show()
    plt.savefig("PLP linear.png")


def plp_bar_chart():
    X = 0.5
    width = 0.5

    fig, ax = plt.subplots(figsize=(12, 7), label='PLP bar chart')
    ax.bar(X, sum(y_plp_decision_tree) / 5, width, label='PLP DECISION TREE')
    ax.bar(X + width, sum(y_plp_random_forest) / 5, width, label='PLP RANDOM FOREST')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("PLP bar chart", fontsize=15)
    # plt.show()
    plt.savefig("PLP bar chart.png")


def spec_cent_result_linear():
    X = [1, 2, 3, 4, 5]
    plt.figure(figsize=(12, 7), label='SPECTRAL CENTROID results')

    # Графики по классификатору decision tree
    plt.plot(X, y_spec_cent_decision_tree, 'r', label="SPECTRAL CENTROID DECISION TREE")
    plt.plot(X, y_spec_cent_random_forest, 'g', label="SPECTRAL CENTROID RANDOM FOREST")
    plt.legend()
    plt.xticks([])
    plt.title("SPECTRAL CENTROID linear", fontsize=15)
    # plt.show()
    plt.savefig("SPECTRAL CENTROID linear.png")


def spec_cent_bar_chart():
    X = 0.5
    width = 0.5

    fig, ax = plt.subplots(figsize=(12, 7), label='SPECTRAL CENTROID bar chart')
    ax.bar(X, sum(y_spec_cent_decision_tree) / 5, width, label='SPECTRAL CENTROID DECISION TREE')
    ax.bar(X + width, sum(y_spec_cent_random_forest) / 5, width, label='SPECTRAL CENTROID RANDOM FOREST')

    ax.set_ylabel('%')
    ax.legend()
    ax.set_xticklabels([])
    plt.title("SPECTRAL CENTROID bar chart", fontsize=15)
    # plt.show()
    plt.savefig("SPECTRAL CENTROID bar chart.png")


print("1 - MFCC linear")
print("2 - MFCC bar chart")
print("3 - LFCC linear")
print("4 - LFCC bar chart")
print("5 - PLP linear")
print("6 - PLP bar chart")
print("7 - spec cent linear")
print("8 - spec cent bar chart")
choose = int(input("Enter choose: "))
if choose == 1:
    mfcc_result_linear()
elif choose == 2:
    mfcc_bar_chart()
elif choose == 3:
    lfcc_result_linear()
elif choose == 4:
    lfcc_bar_chart()
elif choose == 5:
    plp_result_linear()
elif choose == 6:
    plp_bar_chart()
elif choose == 7:
    spec_cent_result_linear()
elif choose == 8:
    spec_cent_bar_chart()