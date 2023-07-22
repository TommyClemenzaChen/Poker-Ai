// result.js
import * as React from "react";
import {Image, StyleSheet, Pressable, Text, View} from "react-native";
import {useNavigation} from "@react-navigation/native";
import { FontFamily, Color } from "./GlobalStyles";

const Results = () => {
  	const navigation = useNavigation();
  	
  	return (
    		<View style={[styles.results, styles.iconLayout]}>
      			<View style={[styles.backParent, styles.backParentFlexBox]}>
        				<Pressable style={[styles.back1, styles.backLayout]} onPress={()=>{}}>
          					<Image style={[styles.icon, styles.iconLayout]} resizeMode="cover" source="back.png" />
        				</Pressable>
        				<View style={[styles.resultsWrapper, styles.backParentFlexBox]}>
          					<Text style={styles.results1}>Results</Text>
        				</View>
        				<View style={[styles.back2, styles.backLayout]} />
      			</View>
      			<View style={[styles.stringValueParent, styles.parentPosition]}>
        				<Text style={[styles.stringValue, styles.detailsTypo]}>String value</Text>
        				<View style={styles.emoji}>
          					<View style={[styles.frameParent, styles.frameParentBg]}>
            						<View style={[styles.vectorParent, styles.parentPosition]}>
              							<Image style={styles.vectorIconLayout} resizeMode="cover" source="Vector.png" />
              							<Image style={[styles.vectorIcon1, styles.vectorIconLayout]} resizeMode="cover" source="Vector.png" />
            						</View>
            						<Image style={[styles.frameChild, styles.frameLayout]} resizeMode="cover" source="Line 6.png" />
            						<Image style={[styles.frameItem, styles.frameLayout]} resizeMode="cover" source="Line 7.png" />
          					</View>
          					<Image style={styles.emojiChild} resizeMode="cover" source="Group 1.png" />
        				</View>
        				<View style={[styles.detailsWrapper, styles.frameParentBg]}>
          					<Text style={[styles.details, styles.detailsTypo]}>Details</Text>
        				</View>
      			</View>
    		</View>);
};

const styles = StyleSheet.create({
  	iconLayout: {
    		width: "100%",
    		overflow: "hidden"
  	},
  	backParentFlexBox: {
    		justifyContent: "space-between",
    		flexDirection: "row"
  	},
  	backLayout: {
    		width: 48,
    		height: 48
  	},
  	parentPosition: {
    		left: "50%",
    		position: "absolute"
  	},
  	detailsTypo: {
    		fontFamily: FontFamily.plusJakartaSansExtrabold,
    		fontWeight: "800",
    		textAlign: "left"
  	},
  	frameParentBg: {
    		backgroundColor: Color.white,
    		overflow: "hidden"
  	},
  	vectorIconLayout: {
    		height: 52,
    		width: 24
  	},
  	frameLayout: {
    		height: 24,
    		width: 16,
    		left: 86,
    		position: "absolute"
  	},
  	icon: {
    		height: "100%",
    		overflow: "hidden"
  	},
  	back1: {
    		height: 48
  	},
  	results1: {
    		fontSize: 16,
    		fontWeight: "700",
    		fontFamily: FontFamily.plusJakartaSansBold,
    		textAlign: "left",
    		color: Color.gray_100
  	},
  	resultsWrapper: {
    		width: 95,
    		alignItems: "center",
    		height: 48
  	},
  	back2: {
    		height: 48,
    		overflow: "hidden"
  	},
  	backParent: {
    		top: 0,
    		left: 0,
    		borderColor: "#3f3f3f",
    		borderBottomWidth: 0.5,
    		width: 390,
    		height: 90,
    		alignItems: "flex-end",
    		borderStyle: "solid",
    		position: "absolute",
    		overflow: "hidden"
  	},
  	stringValue: {
    		fontSize: 46,
    		color: Color.gray_100,
    		fontWeight: "800"
  	},
  	vectorIcon1: {
    		marginLeft: 50
  	},
  	vectorParent: {
    		marginLeft: -41,
    		top: 56,
    		flexDirection: "row"
  	},
  	frameChild: {
    		top: 106
  	},
  	frameItem: {
    		top: 122
  	},
  	frameParent: {
    		width: "98.2%",
    		top: "0%",
    		right: "1.8%",
    		bottom: "0%",
    		left: "0%",
    		borderRadius: 100,
    		borderColor: "#000",
    		borderWidth: 8,
    		height: "100%",
    		borderStyle: "solid",
    		position: "absolute"
  	},
  	emojiChild: {
    		height: "28.09%",
    		width: "30.72%",
    		top: "60%",
    		right: "-2.18%",
    		bottom: "11.91%",
    		left: "71.47%",
    		maxWidth: "100%",
    		maxHeight: "100%",
    		position: "absolute",
    		overflow: "hidden"
  	},
  	emoji: {
    		width: 183,
    		height: 180,
    		marginTop: 60
  	},
  	details: {
    		fontSize: 20,
    		color: "#000"
  	},
  	detailsWrapper: {
    		borderRadius: 30,
    		paddingHorizontal: 81,
    		paddingVertical: 10,
    		justifyContent: "center",
    		marginTop: 60,
    		alignItems: "center",
    		flexDirection: "row"
  	},
  	stringValueParent: {
    		marginTop: -201.5,
    		marginLeft: -132,
    		top: "50%",
    		alignItems: "center"
  	},
  	results: {
    		backgroundColor: "#252525",
    		flex: 1,
    		height: 844,
    		overflow: "hidden"
  	}
});

export default Results;