import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import Checkbox from 'expo-checkbox';

const customInput = () => {
  const [card1, setCard1] = React.useState('');
  const [card2, setCard2] = React.useState('');
  const [checked, checkTheBox] = React.useState(false);

  //Possible inputs for drop down box
  const data = [
    { key: '1', value: 'A' },
    { key: '2', value: '2' },
    { key: '3', value: '3' },
    { key: '4', value: '4' },
    { key: '5', value: '5' },
    { key: '6', value: '6' },
    { key: '7', value: '7' },
    { key: '8', value: '8' },
    { key: '9', value: '9' },
    { key: '10', value: '10' },
    { key: '11', value: 'Jack' },
    { key: '12', value: 'Queen' },
    { key: '13', value: 'King' },
  ];

  return (
    <View style={styles.outerContainer}>
      <View style={styles.container}>
        <Text style={styles.header}>Select your cards</Text>

        <View style={styles.cardWrapper}>
          <SelectList
            data={data}
            setSelected={setCard1}
            dropdownStyles={styles.dropdown}
            placeholder="Select a card"
          />
        </View>

        <View style={styles.cardWrapper}>
          <SelectList
            data={data}
            setSelected={setCard2}
            dropdownStyles={styles.dropdown}
            placeholder="Select a card"
          />
        </View>

        <View style={styles.checkboxContainer}>
          <Text style={styles.checkBoxText}>Suited?</Text>
          <Checkbox
            style={styles.checkBox}
            value={checked}
            onValueChange={checkTheBox}
          />
        </View>

        <TouchableOpacity
          style={styles.button}
          onPress={() =>
            alert(
              data.find((item) => item.key === card1)?.value +
                ', ' +
                data.find((item) => item.key === card2)?.value +
                '\n' +
                (checked ? 'Suited' : 'Not Suited')
            )
          }
        >
          <Text style={styles.buttonText}>Submit</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  outerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  container: {
    backgroundColor: 'white',
    paddingVertical: 40,
    paddingHorizontal: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  header: {
    fontSize: 25,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  cardWrapper: {
    marginTop: 20,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    padding: 5,
  },
  dropdown: {
    backgroundColor: 'white',
  },
  checkboxContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 30,
  },
  checkBox: {
    borderRadius: 2,
    borderWidth: 2,
    borderColor: 'coral',
    backgroundColor: 'transparent',
    marginLeft: 20,
  },
  checkBoxText: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: 'orange',
    borderRadius: 10,
    paddingVertical: 15,
    paddingHorizontal: 30,
    marginTop: 20,
  },
  buttonText: {
    fontSize: 15,
    fontWeight: 'bold',
    textAlign: 'center',
    color: 'white',
  },
});

export default customInput;
