import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native'; // <-- Import useNavigation
const StarterPage = () => {
  const navigation = useNavigation(); // <-- Get the navigation object

  const handlePlayButton = () => {
    navigation.navigate('StudyPage'); // Navigate to the StudyPage screen
  };

  

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Poker AI</Text>
      <TouchableOpacity style={styles.button} onPress={handlePlayButton}>
        <Text style={styles.buttonText}>Play</Text>
      </TouchableOpacity>
      
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#252525',
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 50,
  },
  button: {
    backgroundColor: '#EABF6F',
    borderRadius: 10,
    paddingVertical: 15,
    paddingHorizontal: 30,
    marginBottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});

export default StarterPage;
