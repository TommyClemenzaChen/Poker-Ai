import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const StarterPage = () => {
  const navigation = useNavigation();

  const handlePlayButton = () => {
    navigation.navigate('StudyPage');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Poker AI</Text>
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
