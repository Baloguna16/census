import os
import csv
import numpy as np
import pandas as pd

def by_year(file='data/raw_1976-2018.csv'):
    i = 0
    raw_data = pd.read_csv(file, header=None)
    while i < len(raw_data):
        row = raw_data.iloc[[i]]
        year = str(row.iloc[0][0])
        row.to_csv("data/by_year/elections_{}.csv".format(year),
            index=False,
            header=False,
            mode='a')
        i += 1

def by_win(file=None):
    if file is None:
        for f in os.listdir('data/by_year'):
            raw_data = pd.read_csv('data/by_year/' + f, header=None)
            i = 0
            most_votes = 0
            total_votes = int(raw_data.iloc[[i]].iloc[0][16])
            year = str(raw_data.iloc[[i]].iloc[0][0])
            while i < len(raw_data):
                row = raw_data.iloc[[i]]
                votes = int(row.iloc[0][15])
                if votes > most_votes:
                    most_votes = votes
                    if int(row.iloc[0][16]) == total_votes:
                        winning_row = raw_data.iloc[[i]]
                if int(row.iloc[0][16]) != total_votes:
                    total_votes = int(row.iloc[0][16])
                    winning_row.to_csv("data/by_win/elections_{}.csv".format(year),
                        index=False,
                        header=False,
                        mode='a')
                    winning_row = raw_data.iloc[[i]]
                    most_votes = votes
                i += 1
            winning_row.to_csv("data/by_win/elections_{}.csv".format(year),
                index=False,
                header=False,
                mode='a')

#Requires the file to have a header. do not edit files in by_win
def by_seats(file=None):
    if file is None:
        for f in os.listdir('data/by_win'):
            raw_data = pd.read_csv('data/by_win/' + f, header=None)
            i = 0
            majority_caucus = ''
            parties = {
                'REPUBLICAN' : 0,
                'DEMOCRAT' : 0,
                'OTHER' : 0
                }
            while i < len(raw_data): #for 50 states
                row = raw_data.iloc[[i]]
                year = str(row.iloc[0][0])
                state = str(row.iloc[0][1])
                state_abbr = str(row.iloc[0][2])
                current_state_abbr = str(row.iloc[0][2])
                total_votes_cast = 0
                while state_abbr == current_state_abbr:
                    if i < len(raw_data):
                        row = raw_data.iloc[[i]]
                        current_state_abbr = str(row.iloc[0][2])
                        if state_abbr == current_state_abbr:
                            total_votes_cast += int(row.iloc[0][16])
                            party = str(row.iloc[0][12]).strip()
                            if party in parties:
                                parties[party] += 1
                            else:
                                parties['OTHER'] += 1
                            i += 1
                    else:
                        current_state_abbr = None
                #year, state, state abbreviation, total votes cast, republican, democrat, other
                writing_row = [year, state, state_abbr, total_votes_cast, parties['REPUBLICAN'], parties['DEMOCRAT'], parties['OTHER']] #+ [tally for tally in parties.values()]
                with open('data/by_seats/elections_{}.csv'.format(year),'a+') as file:
                    wr = csv.writer(file)
                    wr.writerow(writing_row)
                for party in parties:
                    parties[party] = 0

def by_votes(file=None):
    if file is None:
        for f in os.listdir('data/by_year'):
            i = 0
            raw_data = pd.read_csv('data/by_year/' + f, header=None)
            total_votes = int(raw_data.iloc[[i]].iloc[0][16])
            year = str(raw_data.iloc[[i]].iloc[0][0])
            parties = {
                'REPUBLICAN' : 0,
                'DEMOCRAT' : 0,
                'OTHER' : 0
                }
            while i < len(raw_data):
                row = raw_data.iloc[[i]]
                votes = int(row.iloc[0][15])
                state = str(row.iloc[0][1])
                state_abbr = str(row.iloc[0][2])
                current_state_abbr = str(row.iloc[0][2])
                total_votes_cast = 0
                while state_abbr == current_state_abbr:
                    if i < len(raw_data):
                        row = raw_data.iloc[[i]]
                        current_state_abbr = str(row.iloc[0][2])
                        if state_abbr == current_state_abbr:
                            party = str(row.iloc[0][12]).strip()
                            votes = int(row.iloc[0][15])
                            if party in parties:
                                parties[party] += votes
                            else:
                                parties['OTHER'] += votes
                            i += 1
                    else:
                        current_state_abbr = None
                total_votes_cast = parties['REPUBLICAN'] + parties['DEMOCRAT'] + parties['OTHER']
                writing_row = [year, state, state_abbr, total_votes_cast, parties['REPUBLICAN'], parties['DEMOCRAT'], parties['OTHER']] #+ [tally for tally in parties.values()]
                with open('data/by_votes/elections_{}.csv'.format(year),'a+') as file:
                    wr = csv.writer(file)
                    wr.writerow(writing_row)
                for party in parties:
                    parties[party] = 0

def votes_and_seats_by_state_sorted():
    for f in os.listdir('data/analysis/votes_and_seats_by_state'):
        data = csv.reader(open('data/analysis/votes_and_seats_by_state/' + f),delimiter=',')
        sorted_list = sorted(data, key=operator.itemgetter(0))

        with open('data/analysis/votes_and_seats_by_state_sorted/' + f, "a+") as file:
            wr = csv.writer(file)
            for row in sorted_list:
                wr.writerow(row)

def votes_and_seats_by_state():
    for f in os.listdir('data/analysis/votes_and_seats_by_year'):
        i = 0
        raw_data = pd.read_csv('data/analysis/votes_and_seats_by_year/' + f, header=None)
        while i < len(raw_data):
            row = raw_data.iloc[[i]]
            state_abbr = str(row.iloc[0][2])
            row.to_csv('data/analysis/votes_and_seats_by_state/{}_1976-2018.csv'.format(state_abbr),
                index=False,
                header=False,
                mode='a')
            i += 1

def votes_and_seats_by_year():
    for f in os.listdir('data/by_votes'):
        i = 0
        votes_raw_data = pd.read_csv('data/by_votes/' + f, header=None)
        year = str(votes_raw_data.iloc[[i]].iloc[0][0])
        while i < len(votes_raw_data):
            votes_row = votes_raw_data.iloc[[i]]
            state = str(votes_row.iloc[0][1])
            state_abbr = str(votes_row.iloc[0][2])
            total_votes = int(votes_row.iloc[0][3])
            percent_rep_votes = int(votes_row.iloc[0][4]) / int(votes_row.iloc[0][3])
            percent_dem_votes = int(votes_row.iloc[0][5]) / int(votes_row.iloc[0][3])
            percent_other_votes = int(votes_row.iloc[0][6]) / int(votes_row.iloc[0][3])

            seats_raw_data = pd.read_csv('data/by_seats/' + f, header=None)
            seats_row = seats_raw_data.iloc[[i]]
            total_seats = int(seats_row.iloc[0][4]) + int(seats_row.iloc[0][5]) + int(seats_row.iloc[0][6])
            percent_rep_seats = int(seats_row.iloc[0][4]) / total_seats
            percent_dem_seats = int(seats_row.iloc[0][5]) / total_seats
            percent_other_seats = int(seats_row.iloc[0][6]) / total_seats

            writing_row = [
                year,
                state,
                state_abbr,
                total_votes,
                percent_rep_votes,
                percent_dem_votes,
                percent_other_votes,
                total_seats,
                percent_rep_seats,
                percent_dem_seats,
                percent_other_seats
                ]
            with open('data/analysis/votes_and_seats_by_year/elections_{}.csv'.format(year),'a+') as file:
                wr = csv.writer(file)
                wr.writerow(writing_row)
            i += 1
