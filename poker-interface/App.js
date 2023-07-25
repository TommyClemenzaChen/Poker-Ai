import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import StarterPage from './starter';
import customInput from './study';
import Result from './fold';
import {NavigationContainer} from "@react-navigation/native"
import Raise from './raise';
 const Stack = createStackNavigator();

 // This is the main component that contains all the pages
export default function App() {
  return (
  <NavigationContainer>
    <Stack.Navigator> 
      {/* Starter page */}
      <Stack.Screen
        name="StarterPage"
        component={StarterPage}
        options={{ headerShown: false }}
      />
      {/* Study page */}
      <Stack.Screen
        name="StudyPage"
        component={customInput}
        options={{ headerShown: false }}
      />
      {/* Fold page */}
      <Stack.Screen
        name="FoldPage"
        component={Result}
        options={{ headerShown: false }}
      />
      {/* Raise page */}
      <Stack.Screen
        name="RaisePage"
        component={Raise}
        options={{ headerShown: false }}
      />
      
    </Stack.Navigator>
    </NavigationContainer>
  );
};

