#!/bin/bash

# Ce script permet d'afficher des statistiques à propos du dépôt git
# Usage: ./review_stats.sh [commit1] [commit2]

set -e

ORA='\033[0;33m' # Orange
NC='\033[0m' # No Color


if [ ! "$(git rev-parse --is-inside-work-tree 2> /dev/null)" == "true" ]
  then
    echo "Error: You are not in a git repo."
    exit 1
fi

# Le $# revoie le nombre de arguments/paramètres passé au script ./review_stats.sh
# Si nombre d'argument différent de 2
if [ $# -ne 2 ]
  then
    echo "For this script to work, exactly 2 parameters are required (Git commit ID/hash), example : ./review_stats.sh 846d29d cf5956a"
    exit 1
# Si 2 arguments
else
  regexcheckcommit=^[a-f0-9]{7,40}$
  commitone=$1
  committwo=$2
  err=0
  # Si les paramètres ne match pas avec le regex, erreur
  if ! [[ $commitone =~ $regexcheckcommit && $committwo =~ $regexcheckcommit ]]
    then
      echo "Incorrect parameters, these are not Git commit ID/hash, here's an example of parameters : ./review_stats.sh 846d29d cf5956a"
      exit 1
  fi
  # Si le commit n'existe pas, renvoyer une erreur
  if [ ! $(git cat-file -t $commitone 2>/dev/null) ]
    then
      echo -e "Error: $commitone is not a correct commit" # >> /dev/stderr
      err=1
  fi
  if [ ! $(git cat-file -t $committwo 2>/dev/null) ]
    then
      echo -e "Error: $committwo is not a correct commit" # >> /dev/stderr
      err=1
  fi
  if [[ $err == 1 ]]
    then
      exit 1
  fi
  timecommitone=$(git show -s --format=%ct $commitone)
  timecommittwo=$(git show -s --format=%ct $committwo)
  # Si le commit1 est plus ancien que commit2, alors swap les valeurs
  if [ "$timecommitone" -lt "$timecommittwo" ]
    then
      temp=$commitone
      commitone=$committwo
      committwo=$temp
  fi
  # Afficher entre quels commits nous faisons la comparaison
  echo -e "Git repo stats between\n${ORA}${commitone:0:7}${NC} (Newest: $(git show -s --format=%ci $commitone))\n&\n${ORA}${committwo:0:7}${NC} (Oldest: $(git show -s --format=%ci $committwo))\n"
  # Pour afficher les changements entre les commits 1 et 2
  changes=$(echo $(echo -e "$(git diff --stat $commitone $committwo)" | tail -n1) | xargs)
  # Pour afficher le nombre de commit entre 1 et 2
  commit=$(git rev-list --count $commitone $committwo)
  # Pour compter le nombre de pull request qu'il y a eu entre 1 et 2
  # "wc -l" permet de compter le nombre de ligne
  merged=$(git log --merges --oneline $commitone ^$committwo^ | wc -l)
fi

echo -n "Number of commits:"
echo -e "\t$commit"

echo -n "Summary of changes:"
echo -e "\t$changes"

echo -n "Number of merged PRs:"
echo -e "\t$merged"
