// Import necessary libraries and components from react, react-native and react-navigation.
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

// Define the StarterPage component. This is a functional component that renders the start page of your application.
const StarterPage = () => {
  // We use the useNavigation hook to be able to navigate to different screens in the application.
  const navigation = useNavigation();

  // This function is called when the Play button is pressed.
  // It navigates the user to the 'StudyPage' screen.
  const handlePlayButton = () => {
    navigation.navigate('StudyPage');
  };

  // Here we define the UI of the StarterPage. It's a simple page with a title and a Play button.
  return (
    <View style={styles.container}>
      {/* Display the title 'Poker AI' */}
      <Text style={styles.title}>Poker AI</Text>
      {/* Define the 'Play!' button. When it is pressed, the handlePlayButton function is called. */}
      {/* Display the title 'Poker AI' /}
      <Text style={styles.title}>Poker AI</Text>
      {/ Define the 'Play!' button. When it is pressed, the handlePlayButton function is called. */}
      <Text style={styles.title}>Pocket Strategist</Text>
      <TouchableOpacity style={styles.button} onPress={handlePlayButton}>
        <Text style={styles.buttonText}>Play!</Text>
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
    fontSize: 42,
    fontWeight: 'bold',
    fontFamily: 'Plus Jakarta Sans_bold',
    color: 'white',
    marginBottom: 100,
  },
  button: {
    backgroundColor: '#EABF6F',
    borderRadius: 100, // Set to a large value to make it circular
    paddingVertical: 15,
    paddingHorizontal: 30,
    marginBottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    fontFamily: 'Plus Jakarta Sans_bold', // Set the font to cursive
  },
});

export default StarterPage;