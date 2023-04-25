# Author: Luca Soltero
# Email: lsoltero@usc.edu
# Course: Introduction to Econometrics (ECON 318) USC

import Analysis
from matplotlib import pyplot as plt


def join_strings(coefs):
    joined = ' + '.join(coefs)
    return joined


df = Analysis.dataFrame()


class Graph:

    def __init__(self, y, *args):
        self.y = y
        self.args = args

    # def getSummary(self):
    # print(self.model.summary())

    def graphB1(self, title, groupBy):
        fig, ax = plt.subplots()
        for name, group in df.groupby(groupBy):
            if name:
                ax.scatter(group[self.args[0]], group[self.y], color="lightblue", label=f'{groupBy} True',
                           alpha=.7)
            else:
                ax.scatter(group[self.args[0]], group[self.y], color="yellow", label=f'{groupBy} False', alpha=.7)
        # ax.plot(df[self.args[0]], self.model.predict(df[self.args[0]]), color="red", alpha=.7)

        handles, labels = ax.get_legend_handles_labels()
        handles = [handles[1], handles[0]]
        labels = [labels[1], labels[0]]
        plt.xlabel("Tik Tok Duration e^x Seconds")
        plt.ylabel("% Engagement")
        plt.suptitle(title)
        # plt.title(f'%{self.y.title()} = {self.args[0].title()} * Ln(x1) + error')
        plt.legend(handles, labels)
        plt.show()

    def graphB2(self, title, groupBy):
        fig, ax = plt.subplots()
        for name, group in df.groupby(groupBy):
            if name:
                ax.scatter(group[self.args[0]], group[self.y], color="lightblue", label=f'{self.args[1]} true',
                           alpha=.7)
                # ax.plot(group[self.args[0]], self.model.predict(group), color="blue", label="B2 True")
            else:
                ax.scatter(group[self.args[0]], group[self.y], color="yellow", label=f'{self.args[1]} false', alpha=.7)
                # ax.plot(group[self.args[0]], self.model.predict(group), color="red", label="B2 False")
        plt.xlabel("Tik Tok Duration e^x Seconds")
        plt.ylabel("% Engagement")
        plt.suptitle(title)
        # plt.title(f'%{self.y.title()} = {self.args[0].title()} * Ln(x1) + {self.args[1]} * Ln(x2) + error')
        ax.plot()
        plt.legend()
        plt.show()


def main():
    g = Graph("engagement", "duration")
    g.graphB1("After Log Transformation", "isVerified")


if __name__ == '__main__':
    main()