#!/bin/bash

# Ce script permet d'afficher des statistiques à propos du dépôt git
# Usage: ./review_stats.sh [commit1] [commit2]

set -e

ORA='\033[0;33m'
NC='\033[0m' # No Color

echo -e "Git repo stats between\n${ORA}$1${NC}\n&\n${ORA}$2${NC}\n"

if [ ! "$(git rev-parse --is-inside-work-tree 2> /dev/null)" == "true" ]
  then
    echo "Error: You are not in a git repo."
    exit 1
fi

# Le $# revoie le nombre de arguments/paramètres passé au script ./review_stats.sh
# Si nombre d'argument différent de 2
if [ $# -lt 2 -o $# -gt 2 ]
  then
    echo "For this script to work, exactly 2 parameters are required, example : ./review_stats.sh 846d29d cf5956a"
    exit 1
fi

# Si 1 argument
#if [ $# -eq 1 ]
#  then
#    commit=$(git rev-list --count $1)
#fi

# Si 2 arguments
if [ $# -eq 2 ]
  then
    # Pour afficher les changements entre les commits $1 et $2
    # "tail -n1" permet de garder seulement la dernière ligne en sortie de la commande
    # "xargs" permet de retirer les espaces en début et fin de chaîne
    changes=$(echo $(echo -e "$(git diff --stat $1 $2)" | tail -n1) | xargs)
    # Pour afficher le nombre de commit entre $1 et $2
    commit=$(git rev-list --count $1 $2)
    # Pour compter le nombre de pull request qu'il y a eu entre $1 et $2
    # "wc -l" permet de compter le nombre de ligne
    merged=$(git log --merges --oneline $1 ^$2^ | wc -l)
fi

echo -n "Number of commits:"
echo -e "\t$commit"

echo -n "Summary of changes:"
echo -e "\t$changes" | tail -n1

echo -n "Number of merged PRs:"
echo -e "\t$merged"

