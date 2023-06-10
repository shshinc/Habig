import React from 'react';
import {View, StyleSheet, FlatList} from 'react-native';
import FeedListItem from './FeedListItem';

function FeedList({logs, onScrolledToBottom, ListHeaderComponent}) {
 
  return (
    <FlatList
      data={logs}
      style={styles.block}
      renderItem={({item}) => <FeedListItem log={item} />}
      keyExtractor={log => log.id}
      ItemSeparatorComponent={() => <View style={styles.separator} />}
      onScroll={onScroll}
      ListHeaderComponent={ListHeaderComponent}
    />
  );
}