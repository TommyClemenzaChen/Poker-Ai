import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import StarterPage from './starter.js';
import StudyPage from './study.js';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="StarterPage">
        <Stack.Screen name="StarterPage" component={StarterPage} />
        <Stack.Screen name="StudyPage" component={StudyPage} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
