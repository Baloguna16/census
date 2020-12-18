import os
import csv
import random
from time import sleep
import operator
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

def linearize(i, list):
    sorted_list = sorted(list)
    scaled_value = list[i] / sorted_list[-1]
    return scaled_value

def distict_comparisons(year='2012'):
    year = year
    raw_data = pd.read_csv('data/by_win/elections_{}.csv'.format(year), header=None)
    i = 0
    while i < len(raw_data):
        row = raw_data.iloc[[i]]
        state_abbr = row.iloc[0][2]
        current_state_abbr = row.iloc[0][2]

        district_name = []
        percent_vote = []
        total_votes = []
        party = []
        while state_abbr == current_state_abbr:
            row = raw_data.iloc[[i]]
            current_state_abbr = row.iloc[0][2]
            if state_abbr == current_state_abbr:
                district_name.append(str(row.iloc[0][2]) + "-" + str(row.iloc[0][7]))
                percent_vote.append(int(row.iloc[0][15]) / int(row.iloc[0][16]))
                total_votes.append(int(row.iloc[0][16]))
                if isinstance(row.iloc[0][12], str):
                    party.append(row.iloc[0][12][0])
                else:
                    party.append('NA')
                #district_stats[district_name] = (party, percent_vote, total_votes)
                i += 1

        x_pos = [j for j, _ in enumerate(district_name)]

        fig = plt.bar(x_pos, percent_vote)
        plt.xlabel("State-District")
        plt.ylabel("Percent of Vote")
        plt.gca().set_ylim([0.0,1.1])
        plt.gca().set_xlim([0.0,1.1])
        plt.title("Percent of vote required to win by district in {}, {}".format(state_abbr, year))
        plt.xticks(x_pos, district_name, rotation='vertical')

        for k in range(len(party)):
            if party[k] == 'R':
                color = 'red'
            elif party[k] == 'D':
                color = 'blue'
            else:
                color = 'gray'
            fig[k].set_color(color)

        for l in range(len(total_votes)):
            fig[l].set_alpha(linearize(l, total_votes))

        plt.text(0.05, 1.05, "Intensity indicates turnout relative to other districts")
        plt.subplots_adjust(bottom=0.2)
        plt.savefig('data/analysis/graphs/districts_{}/{}_{}.png'.format(year, state_abbr, year))
        plt.clf()
        sleep(1)

def votes_vs_seats_by_year_graph_rep():
    for f in os.listdir('data/analysis/votes_and_seats_by_state_sorted'):
        years = []
        rep_votes_percentages = []
        rep_seats_percentages = []
        with open('data/analysis/votes_and_seats_by_state_sorted/' + f, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in csv_reader:
                years.append(int(row[0]))
                rep_votes_percentages.append(float("{:.2f}".format(float(row[4]))))
                rep_seats_percentages.append(float("{:.2f}".format(float(row[8]))))

        fig, axes = plt.subplots()
        axes.scatter(rep_seats_percentages, rep_votes_percentages, c='red', alpha=0.5, label="ratio of votes-to-seats")
        plt.plot([0.0, 1.0], [0.0, 1.0], color='black', linewidth=1, linestyle='dashed', label="\"Perfect\" Representation")

        for i, txt in enumerate(years):
            axes.annotate(txt, (rep_seats_percentages[i], rep_votes_percentages[i]))

        plt.xlabel('% of seats') #set x axis label
        plt.ylabel('% of votes') #set y axis label
        plt.gca().set_ylim([0.0,1.1])
        plt.gca().set_xlim([0.0,1.1])
        plt.legend()
        plt.title('Votes-to-Seats Ratio in {} (Republican), Total # of Seats: {}'.format(f[:2], str(row[7])))
        plt.savefig('data/analysis/graphs/by_state_votes_vs_seats/{}_rep_percent.png'.format(f[:2]))
        plt.clf()
        sleep(2)

def votes_and_seats_by_year_graph_rep():
    for f in os.listdir('data/analysis/votes_and_seats_by_state_sorted'):
        years = []
        rep_votes_percentages = []
        rep_seats_percentages = []
        with open('data/analysis/votes_and_seats_by_state_sorted/' + f, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in csv_reader:
                years.append(int(row[0]))
                rep_votes_percentages.append(float("{:.2f}".format(float(row[4]))))
                rep_seats_percentages.append(float("{:.2f}".format(float(row[8]))))

        plt.plot( years, rep_votes_percentages, color='red', linewidth=4, label="votes")
        plt.plot( years, rep_seats_percentages, color='red', linewidth=2, linestyle='dashed', label="seats: {} total seats".format(str(row[7])))

        plt.xlabel('years') #set x axis label
        plt.ylabel('percentage') #set y axis label
        plt.gca().set_ylim([0.0,1.1])
        plt.legend()
        plt.title('Relationship between votes and seats in {} (Republican)'.format(f[:2]))
        plt.savefig('data/analysis/graphs/by_state/{}_rep_percent.png'.format(f[:2]))
        plt.clf()
        sleep(2)

def votes_vs_seats_by_year_graph_dem():
    for f in os.listdir('data/analysis/votes_and_seats_by_state_sorted'):
        years = []
        dem_votes_percentages = []
        dem_seats_percentages = []
        with open('data/analysis/votes_and_seats_by_state_sorted/' + f, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in csv_reader:
                years.append(int(row[0]))
                dem_votes_percentages.append(float("{:.2f}".format(float(row[5]))))
                dem_seats_percentages.append(float("{:.2f}".format(float(row[9]))))

        fig, axes = plt.subplots()
        axes.scatter(dem_seats_percentages, dem_votes_percentages, c='blue', alpha=0.5, label="ratio of votes-to-seats")
        plt.plot([0.0, 1.0], [0.0, 1.0], color='black', linewidth=1, linestyle='dashed', label="\"Perfect\" Representation")

        for i, txt in enumerate(years):
            axes.annotate(txt, (dem_seats_percentages[i], dem_votes_percentages[i]))

        plt.xlabel('% of seats') #set x axis label
        plt.ylabel('% of votes') #set y axis label
        plt.gca().set_ylim([0.0,1.1])
        plt.gca().set_xlim([0.0,1.1])
        plt.legend()
        plt.title('Votes-to-Seats Ratio in {} (Democrat), Total # of Seats: {}'.format(f[:2], str(row[7])))
        plt.savefig('data/analysis/graphs/by_state_votes_vs_seats/{}_dem_percent.png'.format(f[:2]))
        plt.clf()
        sleep(2)

def votes_and_seats_by_year_graph_dem():
    for f in os.listdir('data/analysis/votes_and_seats_by_state_sorted'):
        years = []
        dem_votes_percentages = []
        dem_seats_percentages = []
        with open('data/analysis/votes_and_seats_by_state_sorted/' + f, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in csv_reader:
                years.append(int(row[0]))
                dem_votes_percentages.append(float("{:.2f}".format(float(row[5]))))
                dem_seats_percentages.append(float("{:.2f}".format(float(row[9]))))

        plt.plot( years, dem_votes_percentages, color='blue', linewidth=4, label="votes")
        plt.plot( years, dem_seats_percentages, color='blue', linewidth=2, linestyle='dashed', label="seats: {} total seats".format(str(row[7])))

        plt.xlabel('years') #set x axis label
        plt.ylabel('percentage') #set y axis label
        plt.gca().set_ylim([0.0,1.1])
        plt.legend()
        plt.title('Relationship between votes and seats in {} (Democrat)'.format(f[:2]))
        plt.savefig('data/analysis/graphs/by_state/{}_rep_percent.png'.format(f[:2]))
        plt.clf()
        sleep(2)
