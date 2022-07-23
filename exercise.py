from pprint import pprint

#slots:
#0 is not a parking
#1 is occupied
#2 is available
parking_state = [
  [1,1,1], 
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(matrix):
    state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}

    # for each column
    for i in range(len(matrix)):
        # for each row
        for j in range(len(matrix[i])):

            # if current slot is occupied
            if matrix[i][j] == 1:
                state['occupied_slots'] += 1
                state['total_slots'] += 1
            # if current slot is available
            elif matrix[i][j] == 2:
                state['available_slots'] += 1
                state['total_slots'] += 1

    return state

print(get_parking_lot(parking_state))

